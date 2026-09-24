#!/usr/bin/env python3
"""Render an original Turkish explainer animation about NSAID pharmacology."""

from __future__ import annotations

import math
import subprocess
from dataclasses import dataclass
from pathlib import Path

from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
BUILD = ROOT / "build"
OUT = ROOT / "nsaid_etki_mekanizmasi.mp4"
WIDTH, HEIGHT, FPS = 1280, 720, 30

BG = "#081525"
PANEL = "#10243a"
WHITE = "#f4f7fb"
MUTED = "#aac0d5"
CYAN = "#36d1dc"
BLUE = "#4e8cff"
GREEN = "#44d17a"
YELLOW = "#ffc857"
RED = "#ff5c70"
PURPLE = "#a78bfa"

FONT_REG = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"


@dataclass(frozen=True)
class Scene:
    key: str
    title: str
    narration: str
    kind: str
    minimum: float = 7.0


SCENES = [
    Scene(
        "01_intro",
        "NSAİİ’ler nasıl etki eder?",
        "İbuprofen, naproksen, aspirin ve selekoksib; nonsteroid antiinflamatuvar ilaçlar, yani NSAİİ’ler grubundadır. "
        "Ağrı, ateş ve inflamasyonu azaltan ortak hedefleri, siklooksijenaz enzimleridir.",
        "intro",
        9,
    ),
    Scene(
        "02_pathway",
        "Hücre zarından prostanoidlere",
        "Doku hasarı olduğunda hücre zarı fosfolipitlerinden araşidonik asit açığa çıkar. "
        "COX-1 ve COX-2 enzimleri bunu PGH2 adlı ortak bir ara ürüne dönüştürür. "
        "Dokular, PGH2’den prostaglandinler, prostasiklin ve tromboksan üretir.",
        "pathway",
        12,
    ),
    Scene(
        "03_effect",
        "NSAİİ: COX basamağında fren",
        "NSAİİ’ler COX aktivitesini azaltınca bu ürünlerin sentezi de azalır. "
        "Özellikle PGE2 azalınca ağrı sinirlerinin duyarlılığı, inflamatuvar yanıt ve hipotalamustaki ateş sinyali zayıflar. "
        "Sonuç; analjezik, antipiretik ve antiinflamatuvar etkidir.",
        "block",
        13,
    ),
    Scene(
        "04_cox",
        "COX-1 ve COX-2",
        "COX-1 çoğu dokuda sürekli çalışır; mide mukozasının korunmasına, trombosit işlevine ve böbrek kan akımına katkı sağlar. "
        "COX-2 inflamasyonda belirgin biçimde artar. Ancak böbrek, beyin ve damarlar gibi dokularda normal görevleri de vardır. "
        "Bu nedenle COX-1 iyi, COX-2 kötü demek doğru değildir.",
        "cox",
        15,
    ),
    Scene(
        "05_classes",
        "Seçicilik bir spektrumdur",
        "İbuprofen ve naproksen gibi non-selektif ilaçlar COX-1 ve COX-2’yi birlikte inhibe eder. "
        "Selekoksib, terapötik dozlarda COX-2’ye daha seçicidir. Seçicilik mutlak değil, doz ve ilaca göre değişen bir spektrumdur.",
        "classes",
        12,
    ),
    Scene(
        "06_aspirin",
        "Aspirinin özel farkı",
        "Çoğu NSAİİ COX enzimine geri dönüşümlü bağlanır. Aspirin ise enzimi geri dönüşümsüz asetiller. "
        "Trombositler yeni enzim üretemediği için düşük doz aspirinin tromboksan azaltıcı etkisi, o trombositin yaşamı boyunca sürer.",
        "aspirin",
        12,
    ),
    Scene(
        "07_safety",
        "Etki ile yan etki aynı yolaktan doğar",
        "Koruyucu prostaglandinlerin azalması mide ülseri ve kanama, böbrek işlevinde bozulma, sıvı tutulumu ve tansiyon artışına yol açabilir. "
        "Aspirin dışındaki NSAİİ’ler kalp krizi ve inme riskini de artırabilir. Risk; ilaca, doza, kullanım süresine ve kişiye göre değişir.",
        "safety",
        15,
    ),
    Scene(
        "08_summary",
        "Özet",
        "Kısaca: NSAİİ’ler COX enzimlerini inhibe eder, prostanoid sentezini azaltır; böylece ağrı, ateş ve inflamasyon hafifler. "
        "Fakat aynı yolak mideyi, böbreği, trombositleri ve damarları da etkiler. Bu video eğitim amaçlıdır; kişisel tedavi önerisi değildir.",
        "summary",
        13,
    ),
]


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)


def rounded(draw: ImageDraw.ImageDraw, box, radius=22, fill=PANEL, outline=None, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def centered(draw: ImageDraw.ImageDraw, xy, text, fnt, fill=WHITE):
    draw.text(xy, text, font=fnt, fill=fill, anchor="mm")


def arrow(draw: ImageDraw.ImageDraw, start, end, color=CYAN, width=8, phase=0.0):
    x1, y1 = start
    x2, y2 = end
    draw.line((x1, y1, x2, y2), fill=color, width=width)
    angle = math.atan2(y2 - y1, x2 - x1)
    length = 20
    for delta in (2.55, -2.55):
        draw.line(
            (x2, y2, x2 + length * math.cos(angle + delta), y2 + length * math.sin(angle + delta)),
            fill=color,
            width=width,
        )
    for i in range(3):
        t = (phase + i / 3) % 1
        x, y = x1 + (x2 - x1) * t, y1 + (y2 - y1) * t
        draw.ellipse((x - 5, y - 5, x + 5, y + 5), fill=WHITE)


def molecule(draw, center, color, label, pulse=0.0, radius=46):
    x, y = center
    r = radius + 3 * math.sin(pulse * math.tau)
    draw.ellipse((x - r, y - r, x + r, y + r), fill=color)
    centered(draw, (x, y), label, font(22, True), BG)


def wrap(draw, text, fnt, max_width):
    words = text.split()
    lines, line = [], ""
    for word in words:
        test = f"{line} {word}".strip()
        if draw.textlength(test, font=fnt) <= max_width:
            line = test
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def subtitle(draw, text):
    rounded(draw, (70, 615, 1210, 695), radius=18, fill="#06101ddd")
    lines = wrap(draw, text, font(24), 1080)
    y = 655 - (len(lines) - 1) * 15
    for line in lines[:2]:
        centered(draw, (640, y), line, font(24), WHITE)
        y += 30


def header(draw, title, progress):
    draw.text((55, 38), title, font=font(40, True), fill=WHITE)
    draw.rounded_rectangle((55, 98, 1225, 106), radius=4, fill="#20384f")
    draw.rounded_rectangle((55, 98, 55 + 1170 * progress, 106), radius=4, fill=CYAN)


def render_scene(scene: Scene, t: float, duration: float) -> Image.Image:
    img = Image.new("RGB", (WIDTH, HEIGHT), BG)
    d = ImageDraw.Draw(img, "RGBA")
    p = min(1.0, t / duration)
    phase = t * 0.28
    header(d, scene.title, p)

    if scene.kind == "intro":
        for i, (name, col) in enumerate((("İbuprofen", BLUE), ("Naproksen", PURPLE), ("Aspirin", YELLOW), ("Selekoksib", GREEN))):
            x = 190 + i * 300
            y = 275 + 12 * math.sin(t * 1.4 + i)
            rounded(d, (x - 110, y - 52, x + 110, y + 52), 25, col)
            centered(d, (x, y), name, font(26, True), BG)
        centered(d, (640, 440), "Ortak hedef", font(27), MUTED)
        rounded(d, (485, 480, 795, 565), 30, "#173956", outline=CYAN, width=3)
        centered(d, (640, 522), "COX-1  •  COX-2", font(35, True), CYAN)

    elif scene.kind == "pathway":
        labels = [("Hücre zarı", BLUE), ("Araşidonik\nasit", YELLOW), ("COX-1 / COX-2", PURPLE), ("PGH₂", CYAN)]
        xs = [145, 425, 730, 1030]
        for i, ((label, col), x) in enumerate(zip(labels, xs)):
            molecule(d, (x, 285), col, label, phase + i / 4, 64 if i == 2 else 55)
            if i < 3:
                arrow(d, (x + 70, 285), (xs[i + 1] - 75, 285), CYAN, phase=phase)
        for i, (label, col) in enumerate((("PGE₂", RED), ("PGI₂", GREEN), ("TXA₂", YELLOW))):
            x = 835 + i * 165
            arrow(d, (1030, 350), (x, 465), col, 5, phase)
            molecule(d, (x, 500), col, label, phase + i / 3, 40)

    elif scene.kind == "block":
        molecule(d, (220, 320), YELLOW, "Araşidonik\nasit", phase, 62)
        arrow(d, (295, 320), (520, 320), MUTED, phase=phase)
        rounded(d, (520, 250, 755, 390), 28, "#30235b", outline=PURPLE, width=3)
        centered(d, (637, 302), "COX", font(40, True), PURPLE)
        centered(d, (637, 355), "enzimi", font(25), WHITE)
        arrow(d, (755, 320), (1010, 320), MUTED, phase=phase)
        for i in range(3):
            x = 1035 + i * 55
            d.ellipse((x - 24, 296, x + 24, 344), fill=RED)
        x = 637 + 10 * math.sin(t * 2)
        rounded(d, (x - 105, 405, x + 105, 500), 24, RED)
        centered(d, (x, 452), "NSAİİ", font(38, True), WHITE)
        d.line((555, 235, 720, 405), fill=RED, width=15)
        for i, (label, col) in enumerate((("Ağrı ↓", BLUE), ("Ateş ↓", YELLOW), ("İnflamasyon ↓", GREEN))):
            rounded(d, (125 + i * 360, 525, 415 + i * 360, 590), 20, "#122e42", outline=col)
            centered(d, (270 + i * 360, 557), label, font(25, True), col)

    elif scene.kind == "cox":
        for x, label, col in ((330, "COX-1", BLUE), (950, "COX-2", PURPLE)):
            rounded(d, (x - 250, 155, x + 250, 550), 30, "#10243a", outline=col, width=3)
            centered(d, (x, 205), label, font(38, True), col)
        items1 = [("Mide mukozası", "kalkan"), ("Trombosit", "damla"), ("Böbrek kan akımı", "böbrek")]
        items2 = [("İnflamasyonda artar", "alev"), ("Böbrek • beyin", "nokta"), ("Damar işlevleri", "damar")]
        for x, items, col in ((330, items1, BLUE), (950, items2, PURPLE)):
            for i, (label, _) in enumerate(items):
                y = 290 + i * 85
                d.ellipse((x - 185, y - 18, x - 149, y + 18), fill=col)
                d.text((x - 130, y), label, font=font(25), fill=WHITE, anchor="lm")
        centered(d, (640, 580), "“İyi” ve “kötü” değil; farklı ve örtüşen görevler", font(24, True), YELLOW)

    elif scene.kind == "classes":
        d.line((155, 320, 1125, 320), fill="#38536c", width=18)
        d.ellipse((145, 310, 165, 330), fill=WHITE)
        d.ellipse((1115, 310, 1135, 330), fill=WHITE)
        d.text((155, 355), "COX-1 + COX-2", font=font(25, True), fill=BLUE, anchor="mm")
        d.text((1125, 355), "COX-2’ye daha seçici", font=font(25, True), fill=PURPLE, anchor="mm")
        drugs = [("Aspirin", 0.10, YELLOW), ("İbuprofen", 0.25, BLUE), ("Naproksen", 0.38, CYAN), ("Selekoksib", 0.86, GREEN)]
        for i, (name, position, col) in enumerate(drugs):
            x = 155 + 970 * position
            y = 250 - (i % 2) * 65
            d.line((x, y + 30, x, 310), fill=col, width=4)
            rounded(d, (x - 80, y - 25, x + 80, y + 30), 16, col)
            centered(d, (x, y + 2), name, font(21, True), BG)
        centered(d, (640, 480), "Seçicilik ≠ mutlak özgüllük", font(35, True), WHITE)
        centered(d, (640, 535), "Etki; ilaca ve doza göre değişir.", font(25), MUTED)

    elif scene.kind == "aspirin":
        for x, label, color, irreversible in ((345, "Çoğu NSAİİ", BLUE, False), (935, "Aspirin", YELLOW, True)):
            rounded(d, (x - 250, 160, x + 250, 550), 30, PANEL, outline=color, width=3)
            centered(d, (x, 205), label, font(34, True), color)
            rounded(d, (x - 105, 290, x + 105, 405), 28, "#30235b", outline=PURPLE, width=3)
            centered(d, (x, 347), "COX", font(40, True), PURPLE)
            bx = x + (0 if irreversible else 105 * math.sin(t * 1.2))
            rounded(d, (bx - 65, 430, bx + 65, 495), 18, color)
            centered(d, (bx, 462), "İlaç", font(24, True), BG)
            centered(d, (x, 530), "Geri dönüşümsüz" if irreversible else "Geri dönüşümlü", font(24, True), color)
            if irreversible:
                d.arc((x - 32, 325, x + 32, 389), 180, 360, fill=YELLOW, width=8)
                d.rectangle((x - 25, 347, x + 25, 382), fill=YELLOW)
        centered(d, (640, 585), "Trombosit: yeni COX üretemez", font(25, True), RED)

    elif scene.kind == "safety":
        cards = [
            ("Mide", "Ülser • kanama", RED),
            ("Böbrek", "İşlev bozukluğu", BLUE),
            ("Dolaşım", "Sıvı • tansiyon", CYAN),
            ("Kalp / beyin", "MI • inme riski", PURPLE),
        ]
        for i, (organ, risk, col) in enumerate(cards):
            x = 205 + (i % 2) * 610
            y = 205 + (i // 2) * 190
            rounded(d, (x - 145, y - 55, x + 350, y + 85), 25, PANEL, outline=col, width=3)
            d.ellipse((x - 105, y - 15, x - 25, y + 65), fill=col)
            d.text((x + 15, y - 10), organ, font=font(28, True), fill=WHITE)
            d.text((x + 15, y + 35), risk, font=font(23), fill=MUTED)
        centered(d, (640, 570), "Risk = ilaç × doz × süre × kişi", font(30, True), YELLOW)

    elif scene.kind == "summary":
        steps = [("COX inhibisyonu", PURPLE), ("Prostanoid sentezi ↓", CYAN), ("Ağrı • ateş • inflamasyon ↓", GREEN)]
        xs = [225, 640, 1055]
        for i, ((label, col), x) in enumerate(zip(steps, xs)):
            rounded(d, (x - 160, 220, x + 160, 340), 28, PANEL, outline=col, width=3)
            centered(d, (x, 280), label, font(24, True), col)
            if i < 2:
                arrow(d, (x + 170, 280), (xs[i + 1] - 170, 280), MUTED, 6, phase)
        rounded(d, (175, 420, 1105, 545), 25, "#281f16", outline=YELLOW, width=3)
        centered(d, (640, 462), "Fayda ve risk aynı biyolojik yolaktan doğar.", font(31, True), YELLOW)
        centered(d, (640, 510), "Kişisel tedavi için sağlık profesyoneline danışın.", font(24), WHITE)

    subtitle(d, scene.narration)
    return img


def run(command):
    print("+", " ".join(str(part) for part in command))
    subprocess.run(command, check=True)


def duration(path: Path) -> float:
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", path],
        check=True,
        capture_output=True,
        text=True,
    )
    return float(result.stdout.strip())


def render():
    BUILD.mkdir(exist_ok=True)
    segments = []
    for scene in SCENES:
        audio = BUILD / f"{scene.key}.mp3"
        video = BUILD / f"{scene.key}.mp4"
        if not audio.exists():
            gTTS(scene.narration, lang="tr", slow=False).save(audio)
        scene_duration = max(scene.minimum, duration(audio) + 1.0)
        command = [
            "ffmpeg", "-y", "-loglevel", "error",
            "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{WIDTH}x{HEIGHT}", "-r", str(FPS), "-i", "-",
            "-i", str(audio),
            "-filter_complex", f"[1:a]apad=pad_dur={scene_duration:.3f},atrim=duration={scene_duration:.3f},afade=t=in:st=0:d=.15,afade=t=out:st={scene_duration - .35:.3f}:d=.35[a]",
            "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
            "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-t", f"{scene_duration:.3f}", str(video),
        ]
        proc = subprocess.Popen(command, stdin=subprocess.PIPE)
        assert proc.stdin
        total_frames = math.ceil(scene_duration * FPS)
        for frame_no in range(total_frames):
            frame = render_scene(scene, frame_no / FPS, scene_duration)
            proc.stdin.write(frame.tobytes())
        proc.stdin.close()
        if proc.wait() != 0:
            raise RuntimeError(f"ffmpeg failed for {scene.key}")
        segments.append(video)

    concat_file = BUILD / "segments.txt"
    concat_file.write_text("".join(f"file '{segment.as_posix()}'\n" for segment in segments), encoding="utf-8")
    run([
        "ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(concat_file),
        "-c", "copy", "-movflags", "+faststart", str(OUT),
    ])
    print(f"Created {OUT} ({duration(OUT):.1f} seconds)")


if __name__ == "__main__":
    render()
