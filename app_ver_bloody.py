import math
import re
import asyncio
import random
import os
import flet as ft


def main(page: ft.Page):
    # ====== ルートディレクトリ ======
    root_dir = os.path.dirname(os.path.abspath(__file__))

    # ウィンドウアイコン（ここは今まで通りでOK）
    page.window.icon = os.path.join(root_dir, "assets", "triangle_bloody -icon.ico")

    page.title = "TRIANGLE-TOOLKIT yamikawa"
    page.window.width = 340
    page.window.height = 600
    page.window.resizable = False
    page.horizontal_alignment = "center"
    page.vertical_alignment = "start"
    page.padding = 0
    page.bgcolor = "#120914"

    # ====== Colors ======
    pink = "#FF5EA9"
    light_pink = "#FFAED8"
    deep_pink = "#CF2E78"
    input_bg = "#2A2A2A"
    output_bg = "#3A2A35"

    error_text = ft.Text("", color="#FF5EA9", size=13)

    # ====== 入力のサニタイズ ======
    def sanitize_number_input(value: str) -> str:
        return re.sub(r"[^0-9.]", "", value)

    # ====== 計算 ======
    def calc_n(e=None):
        tf_a.value = sanitize_number_input(tf_a.value)
        tf_b.value = sanitize_number_input(tf_b.value)
        tf_c.value = sanitize_number_input(tf_c.value)

        def to_float(v: str):
            if v.strip() == "":
                return None
            try:
                return float(v)
            except ValueError:
                return None

        a_val = to_float(tf_a.value)
        b_val = to_float(tf_b.value)
        c_val = to_float(tf_c.value)

        if a_val is None or b_val is None or c_val is None:
            tf_n.value = ""
            error_text.value = ""
            page.update()
            return

        if b_val**2 < c_val**2:
            tf_n.value = ""
            error_text.value = "b² ≥ c² じゃないと無理だよ…"
            page.update()
            return

        alpha = math.sqrt(b_val**2 - c_val**2)
        beta = a_val - alpha
        n_val = math.sqrt(beta**2 + c_val**2)

        tf_n.value = f"{n_val:.4f}"
        error_text.value = ""
        page.update()

    # ====== クリア ======
    def clear_fields(e):
        tf_a.value = ""
        tf_b.value = ""
        tf_c.value = ""
        tf_n.value = ""
        error_text.value = ""
        page.update()

    # ====== 入力欄 ======
    def make_tf(label: str, width: int):
        return ft.TextField(
            label=label,
            width=width,
            text_size=16,
            border_radius=20,
            bgcolor=input_bg,
            color=light_pink,
            border_color=deep_pink,
            focused_border_color=pink,
            cursor_color=pink,
            label_style=ft.TextStyle(color=light_pink),
            on_change=calc_n,
        )

    tf_a = make_tf("a", 80)
    tf_b = make_tf("b", 80)
    tf_c = make_tf("c", 80)

    tf_n = ft.TextField(
        label="N",
        read_only=True,
        width=220,
        text_size=20,
        border_radius=20,
        bgcolor=output_bg,
        color=light_pink,
        border_color=pink,
        text_align=ft.TextAlign.RIGHT,
        label_style=ft.TextStyle(color=light_pink),
    )

    # ====== タイトル ======
    title = ft.Text(
        "✞  TRIANGLE TOOLKIT  ✞",
        size=18,
        weight=ft.FontWeight.BOLD,
        color=pink,
        style=ft.TextStyle(letter_spacing=1),
    )

    title_container = ft.Container(
        content=title,
        alignment=ft.alignment.center,
    )

    # ====== 画像パス（★ここがポイント） ======
    triangle_image_path = os.path.join(root_dir, "assets", "triangle_bloody.png")

    # ====== ぷにぷにクリアボタン ======
    clear_button = ft.Container(
        content=ft.ElevatedButton(
            text="クリア",
            icon=ft.Icons.CLEAR,
            bgcolor=pink,
            color="#1A1A1A",
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=24),
                padding=ft.Padding(20, 10, 20, 10),
                elevation=6,
            ),
            on_click=clear_fields,
        ),
        alignment=ft.alignment.center,
    )

    # ====== カードUI ======
    card = ft.Container(
        width=300,
        padding=16,
        border_radius=26,
        bgcolor="#242424",
        shadow=ft.BoxShadow(
            blur_radius=25,
            spread_radius=1,
            color="#000000",
            offset=ft.Offset(0, 8),
        ),
        content=ft.Column(
            controls=[
                title_container,
                ft.Container(
                    content=ft.Image(
                        src=triangle_image_path,   # ← 絶対パスで指定
                        width=230,
                        height=120,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    alignment=ft.alignment.center,
                    padding=ft.padding.only(top=4, bottom=12),
                ),
                ft.Container(height=4),
                ft.Row(
                    controls=[tf_a, tf_b, tf_c],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    spacing=6,
                ),
                ft.Container(height=10),
                ft.Row(
                    controls=[tf_n],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Container(height=4),
                error_text,
                ft.Container(height=14),
                clear_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=8,
        ),
    )

    # ====== 血のしずくエフェクト ======
    drops: list[ft.Container] = []

    height = page.window.height or 600
    width = page.window.width or 340

    for _ in range(24):
        size = random.randint(6, 11)
        left = random.randint(0, int(width - size))
        start_top = random.randint(-int(height * 0.8), 0)
        speed = random.uniform(0.7, 1.5)

        drop = ft.Container(
            width=size,
            height=size,
            left=left,
            top=start_top,
            border_radius=size / 2,
            bgcolor="#D8163A",
            opacity=0.85,
            shadow=ft.BoxShadow(
                blur_radius=7,
                color="#5A0615",
                offset=ft.Offset(0, 2),
            ),
        )
        drop.data = {"speed": speed}
        drops.append(drop)

    async def animate_drops():
        while True:
            for d in drops:
                d.top += d.data["speed"]
                if d.top > height:
                    d.top = -random.randint(10, int(height * 0.6))
                    d.left = random.randint(0, int(width - d.width))
            page.update()
            await asyncio.sleep(0.03)

    # ====== 背景＋Stack ======
    bg = ft.Container(
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=["#120914", "#1A1A1A", "#2B0B1D"],
        ),
    )

    content_column = ft.Column(
        controls=[
            ft.Container(height=24),
            card,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    root = ft.Stack(
        expand=True,
        controls=[
            bg,
            *drops,
            content_column,
        ],
    )

    page.add(root)
    page.run_task(animate_drops)


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
