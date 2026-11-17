#!/usr/bin/env python3
"""Valida os eggs do repositório e o manifesto SHA256SUMS."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EGG_GLOB = "programming/**/egg-*.json"
REQUIRED_TOP = ("meta", "name", "docker_images", "startup", "config", "scripts", "variables")
REQUIRED_INSTALL = ("script", "container", "entrypoint")
SUSPICIOUS = (
    re.compile(r"(curl|wget)[^\n|]*\|\s*(ba)?sh", re.IGNORECASE),
    re.compile(r"\beval\b", re.IGNORECASE),
    re.compile(r"base64\s+(-d|--decode)", re.IGNORECASE),
)


def fail(errors: list[str], path: Path, message: str) -> None:
    errors.append(f"{path}: {message}")


def validate_egg(path: Path, errors: list[str]) -> None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(errors, path, f"JSON inválido: {exc}")
        return

    for key in REQUIRED_TOP:
        if key not in data:
            fail(errors, path, f"campo obrigatório ausente: {key}")

    meta = data.get("meta") or {}
    if meta.get("version") not in ("PTDL_v1", "PTDL_v2"):
        fail(errors, path, "meta.version deve ser PTDL_v1 ou PTDL_v2")

    if not str(data.get("name", "")).strip():
        fail(errors, path, "name vazio")

    images = data.get("docker_images")
    if not isinstance(images, dict) or not images:
        fail(errors, path, "docker_images deve ser um objeto não vazio")
    else:
        for label, image in images.items():
            if not isinstance(label, str) or not label.strip():
                fail(errors, path, "docker_images com label inválido")
            if not isinstance(image, str) or not image.strip():
                fail(errors, path, "docker_images com imagem inválida")

    if not str(data.get("startup", "")).strip():
        fail(errors, path, "startup vazio")

    config = data.get("config")
    if not isinstance(config, dict):
        fail(errors, path, "config deve ser um objeto")
    else:
        for key in ("files", "startup", "logs"):
            value = config.get(key)
            if isinstance(value, str):
                try:
                    json.loads(value)
                except Exception:
                    fail(errors, path, f"config.{key} não é JSON válido")
            elif not isinstance(value, dict):
                fail(errors, path, f"config.{key} deve ser string JSON ou objeto")
        if not str(config.get("stop", "")).strip():
            fail(errors, path, "config.stop vazio")

    install = ((data.get("scripts") or {}).get("installation") or {})
    for key in REQUIRED_INSTALL:
        if not str(install.get(key, "")).strip():
            fail(errors, path, f"scripts.installation.{key} vazio")
    script = str(install.get("script", ""))
    for pattern in SUSPICIOUS:
        if pattern.search(script):
            fail(errors, path, f"script de instalação contém padrão suspeito: {pattern.pattern}")

    variables = data.get("variables")
    if not isinstance(variables, list):
        fail(errors, path, "variables deve ser uma lista")
    else:
        for index, var in enumerate(variables):
            if not isinstance(var, dict):
                fail(errors, path, f"variables[{index}] inválida")
                continue
            for key in ("name", "env_variable", "rules", "user_viewable", "user_editable"):
                if key not in var:
                    fail(errors, path, f"variables[{index}] sem {key}")


def validate_manifest(errors: list[str]) -> None:
    manifest = ROOT / "SHA256SUMS"
    if not manifest.is_file():
        fail(errors, manifest, "manifesto ausente")
        return

    listed = set()
    for line in manifest.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split(None, 1)
        if len(parts) != 2 or not re.fullmatch(r"[0-9a-f]{64}", parts[0]):
            fail(errors, manifest, f"linha inválida: {line}")
            continue
        listed.add(parts[1].lstrip("*"))

    actual = {str(path.relative_to(ROOT)) for path in ROOT.glob(EGG_GLOB)}
    for missing in sorted(actual - listed):
        fail(errors, manifest, f"egg não listado: {missing}")
    for extra in sorted(listed - actual):
        fail(errors, manifest, f"arquivo listado que não é egg: {extra}")


def main() -> int:
    errors: list[str] = []
    eggs = sorted(ROOT.glob(EGG_GLOB))
    if not eggs:
        errors.append("nenhum egg encontrado")
    for path in eggs:
        validate_egg(path, errors)
    validate_manifest(errors)

    if errors:
        for error in errors:
            print(f"ERRO: {error}", file=sys.stderr)
        return 1

    print(f"OK: {len(eggs)} egg(s) validado(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
