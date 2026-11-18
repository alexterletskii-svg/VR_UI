#!/usr/bin/env python3
"""Рендерит окна screens/*.html в png/*.png с прозрачным фоном. Запуск: python3 tools/render.py"""
import os, glob
from playwright.sync_api import sync_playwright
root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
os.makedirs(os.path.join(root, "png"), exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1920, "height": 1080})
    for f in sorted(glob.glob(os.path.join(root, "screens", "*.html"))):
        pg.goto("file://" + f); pg.wait_for_timeout(300)
        out = os.path.join(root, "png", os.path.basename(f)[:-5] + ".png")
        pg.locator(".stage").screenshot(path=out, omit_background=True); print("ok", os.path.relpath(out, root))
    b.close()
