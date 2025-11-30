import math
import re
import random
import asyncio
import os
import flet as ft


def main(page: ft.Page):
    # ====== ページ設定 ======
    root_dir = os.path.dirname(os.path.abspath(__file__))
    page.window.icon = os.path.join(root_dir, "assets", "triangle-icon.ico")
    page.title = "TRIANGLE-TOOLKIT"
    page.window.width = 340       # スマホくらいの幅
    page.window.height = 600
    page.window.resizable = False  # 画面サイズ固定
    page.horizontal_alignment = "center"
    page.vertical_alignment = "start"
    page.bgcolor = "#E3F7FF"
    page.padding = 0

    # ====== 配色 ======
    accent_color = "#1FA8FF"   # ボタンなど
    sub_color = "#9ADFFF"      # 入力欄の枠など
    bubble_bg_top = "#E3F7FF"
    bubble_bg_bottom = "#BCE7FF"
    output_bg = "#DDF5FF"

    # ====== TextField 変数 ======
    tf_a: ft.TextField | None = None
    tf_b: ft.TextField | None = None
    tf_c: ft.TextField | None = None
    tf_n: ft.TextField | None = None

    # ====== エラーメッセージ ======
    error_text = ft.Text("", color="#FF4B6A", size=13)

    # ====== 0〜9 と . のみ許可 ======
    def sanitize_number_input(value: str) -> str:
        return re.sub(r"[^0-9.]", "", value)

    # ====== N 計算 ======
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

        if b_val ** 2 < c_val ** 2:
            tf_n.value = ""
            error_text.value = "b² ≥ c² を満たしていません。"
            page.update()
            return

        alpha = math.sqrt(b_val**2 - c_val**2)
        beta = a_val - alpha
        n_val = math.sqrt(beta**2 + c_val**2)

        tf_n.value = f"{n_val:.4f}"
        error_text.value = ""
        page.update()

    # ====== 入力欄 ======
    def make_number_field(label: str) -> ft.TextField:
        return ft.TextField(
            label=label,
            width=90,
            text_size=16,
            border_radius=24,
            bgcolor="#F5FBFF",
            border_color=sub_color,
            focused_border_color=accent_color,
            cursor_color=accent_color,
            on_change=calc_n,
        )

    tf_a = make_number_field("a")
    tf_b = make_number_field("b")
    tf_c = make_number_field("c")

    # ====== N 出力 ======
    tf_n = ft.TextField(
        label="N",
        read_only=True,
        width=160,
        text_size=20,
        border_radius=24,
        bgcolor=output_bg,
        border_color=accent_color,
        text_align=ft.TextAlign.RIGHT,
    )

    # ====== クリアボタン ======
    def clear_fields(e):
        tf_a.value = ""
        tf_b.value = ""
        tf_c.value = ""
        tf_n.value = ""
        error_text.value = ""
        page.update()

    clear_button = ft.ElevatedButton(
        text="クリア",
        icon=ft.Icons.CLEAR,  # ここはあなたの環境仕様に合わせてそのまま
        bgcolor=accent_color,
        color="white",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=24),
        ),
        on_click=clear_fields,
    )

    # ====== 上部：三角形画像（あとで差し替え） ======
    triangle_image = ft.Image(
        src=os.path.join(root_dir, "assets", "triangle.png"),
        width=240,
        height=170,
        fit=ft.ImageFit.CONTAIN,
    )

    # ====== タイトル（サブタイトルなし） ======
    title_text = ft.Text(
        "TRIANGLE TOOLKIT",
        size=22,
        weight=ft.FontWeight.BOLD,
        color="#1279B8",
    )

    # ====== 前面UI ======
    main_ui = ft.Column(
        controls=[
            ft.Container(height=16),
            ft.Container(
                content=title_text,
                alignment=ft.alignment.center,
                margin=ft.margin.only(bottom=4),
            ),
            ft.Container(
                content=triangle_image,
                margin=ft.margin.only(top=4, bottom=4),
                padding=10,
                bgcolor="#F8FDFF",
                border_radius=26,
                border=ft.border.all(1, "#CFEFFF"),
            ),
            ft.Container(
                content=ft.Row(
                    [tf_a, tf_b, tf_c],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                margin=ft.margin.only(top=16, bottom=8),
                padding=ft.padding.symmetric(horizontal=12),
            ),
            ft.Container(
                content=tf_n,
                margin=ft.margin.only(top=4, bottom=4),
                padding=ft.padding.symmetric(horizontal=12),
            ),
            ft.Container(
                content=error_text,
                padding=ft.padding.symmetric(horizontal=12),
            ),
            ft.Container(
                content=clear_button,
                alignment=ft.alignment.center,
                margin=ft.margin.only(top=10),
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=4,
    )

    # ====== 泡（リアル＆下→上） ======
    bubbles: list[ft.Container] = []

    height = page.window.height or 600
    width = page.window.width or 340

    # 小さめの泡を多めに
    for _ in range(15):
        size = random.randint(12, 30)
        left = random.randint(0, int(width - size))
        start_top = random.randint(int(height * 0.7), int(height * 1.1))
        speed = random.uniform(0.6, 1.5)  # 上昇スピード

        bubble = ft.Container(
            width=size,
            height=size,
            left=left,
            top=start_top,
            border_radius=size / 2,
            bgcolor="#FFFFFF",           # 真っ白
            opacity=0.55,                # 半透明
            border=ft.border.all(1, "#E0F7FF"),
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=8,
                color="#BEEBFF",
                offset=ft.Offset(0, -1),
            ),
        )
        bubble.data = {"speed": speed}
        bubbles.append(bubble)

    # ====== 泡アニメーション ======
    async def animate_bubbles():
        while True:
            for b in bubbles:
                speed = b.data["speed"]
                b.top -= speed  # 上方向へ移動

                # 完全に上に抜けたら、下のランダム位置から再スタート
                if b.top + b.height < 0:
                    b.top = height + random.randint(0, int(height * 0.3))
                    b.left = random.randint(0, int(width - b.width))

            page.update()
            await asyncio.sleep(0.03)  # 30〜40fps くらいの感覚

    # ====== Stack で背景＋泡＋UI を重ねる ======
    root = ft.Stack(
        controls=[
            ft.Container(
                expand=True,
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=[bubble_bg_top, bubble_bg_bottom],
                ),
            ),
            *bubbles,
            ft.Container(
                content=main_ui,
                expand=True,
            ),
        ]
    )

    page.add(root)

    # 泡アニメーション開始
    page.run_task(animate_bubbles)


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
