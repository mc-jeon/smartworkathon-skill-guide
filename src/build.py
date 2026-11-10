"""스마트워크톤 트랙B — 스킬 제작 가이드
실행: python src/build.py   → docs/index.html, docs/practice/prompts_all.txt, docs/practice/checklist.txt
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lessonkit import (E, Page, app_window, box, build, cards, dialog, downloads, dropdown, fig, figs, flow, gbtn, hero,
                       kbd, menubar, mk, prompt, section, shot_list_section, step, table, ui, wrap)
from theme_clay import THEME_CSS, add_pager, clay_hero, tab_hero

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
PRACTICE = DOCS / "practice"
SITE_URL = "https://skill-guide.edunfuture.workers.dev/"

# ── 유튜브 영상: 주소를 받으면 여기에 넣고 다시 빌드 ──
VIDEO_URL = "https://youtu.be/ChMliaRgQek"   # 스마트워크톤 홍보영상(확장판)
VIDEO_TITLE = "AI가 처음이어도 괜찮습니다 — 스마트워크톤 이야기"
GUIDE_VIDEO_URL = "https://www.youtube.com/watch?v=nq9JhgFXajE"   # 스킬 제작 가이드 소개영상
GUIDE_TITLE = "스킬 제작 가이드 소개 (54초)"

PC = "프롬프트 붙여넣기·메모장 저장은 PC에서 하세요. 휴대폰에서는 화면 확인·복습용으로 보세요. 그림은 탭하면 크게 볼 수 있습니다."
AI_TITLE = "AI 채팅 (ChatGPT · Claude · Gemini 공통)"

# ───────────────────────── 프롬프트(교안·프롬프트 모음 파일에 같이 쓰임) ─────────────────────────
P_TASTE_1 = "제주 감귤잼 홍보 글 써 줘"

P_TASTE_2 = """아래 상품으로 인스타그램 게시글을 만들어 줘.

[상품 정보]
- 상품명: 귤빛담은 수제 감귤잼
- 상품 특징: 제주 감귤 사용, 비정제 원당 사용, 보존료·색소 무첨가, 유리병 240g
- 홍보 대상: 아이 간식을 고르는 30~40대 부모
- 가격: (제공되지 않음)

[만드는 방법]
1. 홍보 대상이 공감할 첫 문장을 쓴다.
2. 상품 특징 중 대상에게 중요한 것 2~3개를 골라 쉽게 풀어 쓴다.
3. 마지막 줄에 해시태그 5개를 붙인다.

[출력 형식]
첫 문장 1줄 + 본문 5줄 이내 + 해시태그 5개

[규칙]
상품 정보에 없는 가격·성능·후기는 지어내지 말고, 필요하면 [확인 필요]라고 써 줘."""

P_MAKE = """너는 마케팅 업무를 돕는 'AI 스킬'을 설계하는 전문가야.
아래 [과제 조건]을 모두 지키는 '스킬 설명서'를 만들어 줘.
이 설명서는 다른 AI 채팅에 그대로 붙여넣으면 바로 작동해야 해.

[과제 조건]
1. 상품 특징과 홍보 대상을 입력받아 모든 콘텐츠에 반영한다.
2. 콘텐츠마다 제작 절차(순서)와 출력 형식(분량, 구성, 해시태그 수 등)을 정확히 적는다.
3. 특정 상품 이름을 넣지 말고, 어떤 상품이든 다시 쓸 수 있게 만든다.
4. 입력에 없는 성능·가격·수치·인증·후기는 절대 지어내지 않는다. 정보가 없으면 [확인 필요]라고 표시한다.
5. 모든 결과물은 시험용 초안이며, 실제 게시·광고 집행·유료 결제는 하지 않는다.

[내가 만들고 싶은 콘텐츠]
인스타그램 게시글, 네이버 블로그 글, 카카오톡 채널 홍보 메시지

[내 스킬만의 특징]
없음

[스킬 설명서 구성] 아래 번호와 제목을 그대로 써 줘.
0. 스킬 이름과 한 줄 설명
1. 입력받을 정보 (빈칸 양식 포함, 빠진 정보가 있으면 먼저 질문하기)
2. 꼭 지킬 규칙
3. 콘텐츠별 제작 절차와 출력 형식
4. 결과를 내기 전 스스로 점검할 항목
5. 최종 출력 순서

[작성 방법]
- 메모장에 저장할 것이므로 표, 굵은 글씨(**), # 기호, 코드 상자 없이 일반 글자와 번호, - 기호만 써 줘.
- 설명서 본문만 보여 주고, 앞뒤 인사말은 빼 줘."""

P_RUN = """지금부터 붙여넣는 글은 '스킬 설명서'야. 앞으로 이 설명서대로만 일해 줘.
다 읽었으면 다른 말 없이 "상품 정보를 보내 주세요"라고만 답해 줘.
"""

P_NO_PRICE = "가격 정보는 없어. 가격은 [확인 필요]로 두고 그대로 진행해 줘."

P_CHECK = """방금 만든 결과물을 스킬 설명서의 규칙과 비교해서 점검해 줘. 아래 형식으로만 답해 줘.
1. 상품 정보에 없는데 지어낸 내용(성능·가격·수치·후기): 있으면 그 문장을 그대로 옮기고, 없으면 "없음"
2. 홍보 대상이 반영된 곳: 콘텐츠마다 한 줄씩
3. 출력 형식(분량·구성·해시태그 수 등)을 어긴 곳: 있으면 콘텐츠 이름과 함께, 없으면 "없음"
4. 1번이나 3번에 문제가 있었다면, 고친 결과물 전체"""

P_FIX = """스킬 설명서를 시험해 봤더니 아래 문제가 있었어.
문제를 고친 설명서 전체를 처음부터 끝까지 다시 써 줘. (번호와 제목은 그대로, 메모장용 일반 글자로)

[문제]
블로그 글이 너무 길었다"""

P_FINAL = """아래 [과제 조건]과 [내 스킬 설명서]를 비교해서 점검해 줘.
조건마다 "충족 / 부족" 중 하나로 답하고, 부족하면 설명서에 추가할 문장을 알려 줘. 설명서를 새로 쓰지는 마.

[과제 조건]
1. 상품 특징과 홍보 대상을 입력받아 반영하는가
2. 콘텐츠별 제작 절차와 출력 형식이 적혀 있는가
3. 특정 상품에 묶이지 않고 다른 상품에도 다시 쓸 수 있는가
4. 제공되지 않은 성능·가격을 지어내지 말라는 규칙이 있는가
5. 시험용으로만 만들고 실제 게시·유료 결제를 하지 말라는 규칙이 있는가

[내 스킬 설명서]
"""

SAMPLE1 = (PRACTICE / "sample_product_1.txt").read_text(encoding="utf-8").strip()
SAMPLE2 = (PRACTICE / "sample_product_2.txt").read_text(encoding="utf-8").strip()

CHECKLIST = [
    ("요구사항 ①", "상품 특징과 홍보 대상을 입력받는 칸이 설명서 1번에 있다"),
    ("요구사항 ②", "콘텐츠마다 '절차'와 '출력 형식'이 따로 적혀 있다"),
    ("요구사항 ③", "설명서 안에 특정 상품 이름(감귤잼 등)이 없다 / 거치대로도 잘 돌아갔다"),
    ("제약조건", "'지어내지 않는다' 규칙이 있고, 출력물에 받지 않은 가격·수치가 없다"),
    ("제약조건", "'시험용, 실제 게시·결제 안 함' 규칙이 있다"),
    ("제출 형식", "스킬은 .txt 파일 / 샘플 출력물 파일도 함께 준비했다"),
    ("개인정보", "고객 이름·연락처·회사 내부 자료가 들어 있지 않다"),
]

# ───────────────────────── 이 교안 전용 모형 화면 ─────────────────────────
EXTRA_CSS = """
.ai{display:flex;min-height:250px}
.ai-side{width:132px;flex-shrink:0;background:#f4f4f5;border-right:1px solid #e4e4e7;padding:10px 8px;font-size:12px}
.ai-side .new{display:inline-block;padding:5px 10px;border:1px solid #d4d4d8;border-radius:8px;background:#fff;font-weight:700}
.ai-side .hist{color:#71717a;margin:14px 0 4px;font-size:11px}
.ai-side .it{display:block;padding:4px 6px;border-radius:6px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ai-side .it.on{background:#e4e4e7}
.ai .chat{flex:1;min-width:0}
.chat .tools{align-self:flex-start;font-size:12px;color:#5f6368;display:flex;gap:12px;padding-left:4px;margin-top:-4px}
.chat .send{background:#3f4a5c!important}
.np-tabs{display:flex;gap:4px;background:#eef1f5;padding:6px 8px 0}
.np-tab{background:#fff;border-radius:6px 6px 0 0;padding:4px 12px;font-size:12px}
.np-tab.off{background:transparent;color:#666}
.np-text{padding:10px 12px;white-space:pre-wrap;font-family:Consolas,'Malgun Gothic',monospace;font-size:12px;min-height:190px;line-height:1.55}
.np-status{border-top:1px solid #e5e5e5;padding:3px 10px;font-size:11px;color:#666;display:flex;gap:16px;justify-content:flex-end}
.sv-row{display:flex;gap:8px;align-items:center;margin:7px 0;font-size:12.5px}
.sv-row>span:first-child{width:72px;flex-shrink:0;color:#444}
.sv-box{flex:1;border:1px solid #9aa0a6;border-radius:4px;padding:4px 8px;background:#fff}
.ws{padding:14px;background:#202020;color:#fff;min-height:240px}
.ws .q{background:#2d2d2d;border:1px solid #555;border-radius:20px;padding:7px 14px;color:#fff}
.ws .lbl{color:#bbb;font-size:11px;margin:14px 0 6px}
.ws .res{display:flex;gap:10px;align-items:center;background:#3a3a3a;border-radius:8px;padding:10px}
.ws .ico{width:26px;height:26px;border-radius:6px;background:#3d8be6}
.vwrap{max-width:820px;margin:0 auto}
.vpair{display:grid;grid-template-columns:1fr 1fr;gap:20px;width:100%;margin:0}
.vpair .vwrap{max-width:none;margin:0}
.vcap{font-size:14px;font-weight:700;margin:6px 0 0}
@media (max-width:640px){.vpair{grid-template-columns:1fr}}
.video{position:relative;padding-top:56.25%;border-radius:14px;overflow:hidden;background:#0b1f4b;margin:10px 0}
.video iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.video .ph{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff;text-align:center;padding:20px}
.video .ph b{font-size:20px;margin-bottom:6px}
.vlink{font-size:14px}
"""


def ai_window(messages=(), *, marks=None, new_mark=None, hist=("마케팅 스킬 만들기",), hist_on=None, hist_mark=None,
              input_text="메시지를 입력하세요", tools_mark=None, hello="무엇을 도와드릴까요?"):
    """AI 채팅(일반형) — 왼쪽 '새 채팅'·대화 목록 + 가운데 대화. marks={메시지순번:n,'input':n,'send':n}
    tools_mark: 마지막 AI 답 아래 '복사' 아이콘에 번호."""
    marks = marks or {}
    new = '<span class="new">＋ 새 채팅</span>'
    items = []
    for h in hist:
        cls = "it on" if h == hist_on else "it"
        t = f'<span class="{cls}">{E(h)}</span>'
        items.append(mk(t, hist_mark) if (hist_mark and h == hist_on) else t)
    side = f'<div class="ai-side">{mk(new, new_mark) if new_mark else new}<div class="hist">최근 대화</div>{"".join(items)}</div>'
    out = [] if messages else [f'<div class="hello"><b>AI 채팅</b>{E(hello)}</div>']
    for i, (who, text) in enumerate(messages):
        m = f'<div class="msg {who}">{E(text)}</div>'
        out.append(mk(m, marks[i], block=True) if i in marks else m)
    if tools_mark:
        out.append(f'<div class="tools">{mk("⧉ 복사", tools_mark)}<span>👍</span><span>👎</span><span>↻</span></div>')
    inp = f'<span>{E(input_text)}</span>'
    send = '<span class="send">↑</span>'
    inbox = (f'<div class="inbox">{mk(inp, marks["input"]) if "input" in marks else inp}'
             f'{mk(send, marks["send"]) if "send" in marks else send}</div>')
    return (f'<div class="win-top"><span class="win-icon" style="background:#3f4a5c"></span><span class="win-title">{E(AI_TITLE)}</span></div>'
            f'<div class="ai">{side}<div class="chat">{"".join(out)}{inbox}</div></div>')


def notepad(text="", title="제목 없음", *, text_mark=None, marks=None, dd_for=None, overlay="", tabs=None):
    """윈도우 11 메모장"""
    tabs = tabs or [title]
    tab_html = "".join(f'<span class="np-tab{"" if t == title else " off"}">{E(t)}</span>' for t in tabs) + '<span class="np-tab off">＋</span>'
    body = f'<div class="np-text">{E(text)}</div>'
    if text_mark:
        body = mk(body, text_mark, block=True)
    return (f'<div class="win-top"><span class="win-icon" style="background:#2b7bd9"></span><span class="win-title">{E(title)} - 메모장</span></div>'
            f'<div class="np-tabs">{tab_html}</div>{menubar(["파일", "편집", "보기"], marks, dd_for)}{body}'
            f'<div class="np-status"><span>줄 1, 열 1</span><span>100%</span><span>Windows (CRLF)</span><span>UTF-8</span></div>{overlay}')


NP_FILE_MENU = ["새 탭", "열기", "저장", ("다른 이름으로 저장", 3), "모두 저장", "-", "끝내기"]


def save_dialog(name, n_name=None, n_enc=None, n_save=None):
    def row(label, val, n):
        v = f'<span class="sv-box">{E(val)}</span>'
        return f'<div class="sv-row"><span>{E(label)}</span>{mk(v, n) if n else v}</div>'
    body = (row("파일 이름:", name, n_name) + row("파일 형식:", "텍스트 문서(*.txt)", None) + row("인코딩:", "UTF-8", n_enc))
    return dialog("다른 이름으로 저장", body, gbtn("저장", True, n_save) + gbtn("취소"))


def skill_preview():
    return ("0. 스킬 이름과 한 줄 설명\n- 스킬 이름: 상품 하나로 마케팅 콘텐츠 3종 만들기\n- 한 줄 설명: 상품 정보를 받으면 …\n\n"
            "1. 입력받을 정보\n- 상품명:\n- 상품 특징(3~5개):\n- 홍보 대상:\n…\n\n2. 꼭 지킬 규칙\n- 입력에 없는 성능·가격은 지어내지 않는다 …")


# ───────────────────────── 모델별 모형 화면(2026-11-10 실제 화면 기준) ─────────────────────────
MODELS = {
    "gpt": dict(
        name="ChatGPT", url="chatgpt.com", icon="🟢", accent="#10a37f",
        logo="ChatGPT", logo_tools="🔍 ◫", new="새 채팅", new_icon="✎",
        items=[("🖼", "이미지"), ("🕘", "예약"), ("▥", "라이브러리"), ("@", "플러그인"), ("···", "탐색")],
        sections=[("프로젝트", ["📁 새 프로젝트"])], hist_title="최근",
        topright="◌ 임시 채팅", hello="오늘은 무엇을 해볼까요?", placeholder="ChatGPT에게 물어보세요",
        right_icons="🎙", modes=None, profile="● 내 이름",
        tools=["⧉ 복사", "👍", "👎", "🔊", "⤴", "↻"], copy_label="⧉ 복사",
        item_desc={"새 채팅": "새 대화 시작 — 오늘 가장 많이 누르는 버튼", "이미지": "그림 만들기(오늘은 안 씀)",
                   "예약": "정해진 시간에 자동 실행(오늘은 안 씀)", "라이브러리": "만든 이미지·파일 모음(오늘은 안 씀)",
                   "플러그인": "외부 앱 연결(오늘은 안 씀)", "탐색": "GPT 등 추가 기능 둘러보기(오늘은 안 씀)",
                   "프로젝트": "대화를 폴더처럼 묶기(선택 — '트랙B' 프로젝트를 만들어 모아 두면 편함)",
                   "최근": "지난 대화 목록 — 4-3에서 스킬 만든 대화로 돌아갈 때 사용"},
        today={"새 채팅", "최근"},
    ),
    "claude": dict(
        name="Claude", url="claude.ai", icon="🟠", accent="#c96442",
        logo="Claude", logo_tools="💬 ‹/›", new="새로 만들기", new_icon="＋",
        items=[("🔍", "검색"), ("🗂", "프로젝트"), ("⧉", "아티팩트"), ("🧰", "사용자 지정")],
        sections=[("고정됨 ⌄", [])], hist_title="최근 항목 ⌄",
        topright="", hello="✳ 안녕하세요!", placeholder="오늘 어떤 도움을 드릴까요?",
        right_icons="", modes=None, profile="● 내 이름",
        tools=["⧉ 복사", "👍", "👎", "↻ 다시 시도"], copy_label="⧉ 복사",
        item_desc={"새로 만들기": "새 대화 시작 — 다른 AI의 '새 채팅'과 같은 버튼", "검색": "지난 대화 찾기",
                   "프로젝트": "대화와 자료를 묶어 두기(선택)", "아티팩트": "Claude가 만든 문서·화면 모음(오늘은 안 씀)",
                   "사용자 지정": "스타일·연결 설정(오늘은 안 씀)", "고정됨": "자주 쓰는 대화를 위에 고정",
                   "최근 항목": "지난 대화 목록 — 4-3에서 스킬 만든 대화로 돌아갈 때 사용"},
        today={"새로 만들기", "최근 항목"},
    ),
    "gemini": dict(
        name="Gemini", url="gemini.google.com", icon="🔵", accent="#4285f4",
        logo="", logo_tools="🔍 ◫", new="새 채팅", new_icon="✎",
        items=[("⊞", "라이브러리"), ("🖼", "이미지"), ("🕘", "예약"), ("◎", "맞춤설정"), ("···", "더보기")],
        sections=[], hist_title="최근",
        topright="⤓ 앱 설치  ✎", hello="무엇을 도와드릴까요?", placeholder="Gemini에게 물어보기",
        right_icons="🎙", modes=("채팅", "작업"), profile="● 내 이름 · ⚙",
        tools=["👍", "👎", "↻", "⤴", "⧉ 복사", "⋮"], copy_label="⧉ 복사",
        item_desc={"새 채팅": "새 대화 시작 — 오늘 가장 많이 누르는 버튼", "라이브러리": "만든 결과물 모음(오늘은 안 씀)",
                   "이미지": "그림 만들기(오늘은 안 씀)", "예약": "정해진 시간에 자동 실행(오늘은 안 씀)",
                   "맞춤설정": "Gemini에게 알려 둘 내 정보(오늘은 안 씀)", "더보기": "Gem 등 추가 기능",
                   "채팅 / 작업": "입력창 아래 선택 — 오늘은 반드시 '채팅'",
                   "최근": "지난 대화 목록 — 4-3에서 스킬 만든 대화로 돌아갈 때 사용(안 보이면 🔍 검색)"},
        today={"새 채팅", "채팅 / 작업", "최근"},
    ),
}

MODEL_CSS = """
.mw{display:flex;min-height:300px;font-size:12px;color:#1f1f1f;background:#fff}
.mw-side{width:150px;flex-shrink:0;padding:10px 8px;display:flex;flex-direction:column;gap:1px}
.mw-logo{display:flex;justify-content:space-between;align-items:center;font-weight:800;font-size:14px;padding:2px 6px 8px}
.mw-logo small{font-weight:400;font-size:11px;color:#777;letter-spacing:2px}
.mw-it{display:block;padding:4px 6px;border-radius:8px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.mw-it.on{background:rgba(0,0,0,.07)}
.mw-sec{color:#888;font-size:10.5px;margin:10px 6px 2px}
.mw-prof{margin-top:auto;padding:8px 6px 0;font-size:11px;color:#555}
.mw-main{flex:1;min-width:0;display:flex;flex-direction:column;padding:8px 12px 12px;position:relative}
.mw-top{text-align:right;font-size:11px;color:#666;min-height:16px}
.mw-hello{text-align:center;font-size:17px;margin:auto 0 12px;padding-top:40px}
.mw-msgs{display:flex;flex-direction:column;gap:8px;flex:1;padding-top:4px}
.mw-msg{white-space:pre-wrap;line-height:1.5;font-size:11.5px}
.mw-msg.user{align-self:flex-end;max-width:82%;padding:7px 11px;border-radius:16px}
.mw-msg.ai{align-self:flex-start;max-width:96%}
.mw-tools{display:flex;gap:10px;font-size:11px;color:#666;margin-top:-2px}
.mw-in{border:1px solid #dcdcdc;border-radius:22px;padding:9px 12px;display:flex;align-items:center;gap:8px;color:#888;background:#fff;
  box-shadow:0 2px 6px rgba(0,0,0,.05);margin-top:8px}
.mw-in .ph{flex:1;white-space:pre-wrap;overflow:hidden;max-height:58px}
.mw-in .plus{font-size:15px;color:#555}
.mw-in .snd{width:24px;height:24px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;color:#fff;font-size:13px}
.mw-modes{display:flex;justify-content:center;gap:6px;margin-top:8px;font-size:11px}
.mw-modes span{padding:3px 10px;border-radius:999px}
.mw-modes span.on{background:#fff;box-shadow:0 1px 3px rgba(0,0,0,.15)}
.mw-paste{display:inline-block;border:1px solid #d9d4c7;border-radius:8px;padding:5px 8px;background:#fff;font-size:10.5px;color:#555;margin-bottom:4px}
.mw-panel{position:absolute;right:8px;top:30px;bottom:56px;width:44%;background:#fff;border:1px solid #e3ded2;border-radius:10px;
  box-shadow:-6px 0 18px rgba(0,0,0,.08);padding:8px 10px;font-size:10.5px;white-space:pre-wrap;line-height:1.45;overflow:hidden}
.mw-panel .pt{display:flex;justify-content:space-between;font-weight:700;font-size:11px;margin-bottom:6px;white-space:normal}
/* ChatGPT */
.mw-gpt .mw-side{background:#f9f9f9;border-right:1px solid #ececec}
.mw-gpt .mw-msg.user{background:#f2f2f2}
.mw-gpt .snd{background:#0d0d0d}
.mw-gpt .mw-hello{font-size:18px}
/* Claude */
.mw-claude{background:#faf9f5}
.mw-claude .mw-side{background:#f5f4ee;border-right:1px solid #e8e5da}
.mw-claude .mw-logo{font-family:Georgia,'Times New Roman',serif;font-size:16px}
.mw-claude .mw-hello{font-family:Georgia,'Batang',serif;font-size:20px}
.mw-claude .mw-hello::first-letter{color:#d97757}
.mw-claude .mw-msg.user{background:#f0eee6}
.mw-claude .mw-in{border-radius:14px;flex-direction:column;align-items:stretch;gap:6px}
.mw-claude .mw-in .r1{min-height:20px}
.mw-claude .mw-in .r2{display:flex;justify-content:space-between;align-items:center}
.mw-claude .snd{background:#c96442;border-radius:8px}
/* Gemini */
.mw-gemini .mw-side{background:#f8fafd}
.mw-gemini .mw-main{background:radial-gradient(ellipse at 50% 55%,#dbe8fb 0%,#fff 62%)}
.mw-gemini .mw-hello{font-size:19px}
.mw-gemini .mw-msg.user{background:#e9eef6;border-radius:18px 4px 18px 18px}
.mw-gemini .snd{background:#0b57d0}
.mw-gemini .mw-modes span.on{background:#fff}
/* 모델 고르기 카드 */
.pick{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:12px 0 6px}
.pick a{display:block;text-decoration:none;color:var(--ink);padding:18px 18px 16px;border-radius:22px;background:#fff;border:2px solid #eee;
  box-shadow:0 14px 28px -20px rgba(60,50,120,.6);transition:transform .2s}
.pick a:hover{transform:translateY(-4px)}
.pick a b{display:block;font-size:20px;margin:4px 0}
.pick a small{color:#666;font-size:13px;line-height:1.5;display:block}
.pick a .go{display:inline-block;margin-top:10px;font-weight:800;font-size:13.5px}
@media(max-width:640px){.pick{grid-template-columns:1fr}}
.mtable td:first-child{white-space:nowrap;font-weight:700}
"""


def model_window(key, messages=(), *, marks=None, hist=(), hist_on=None, input_text=None, tools=False,
                 paste=None, panel=None, side_on=None, number_menu=False):
    """모델별 실제 화면 배치를 따른 모형. marks 키:
    'new' / 'item:<이름>' / 'sec:<제목>' / 'hist' / 'input' / 'plus' / 'send' / 'copy' / 'mode' / 'panelcopy' / 메시지순번(int)"""
    S = MODELS[key]
    marks = marks or {}
    M = lambda html, k, block=False: mk(html, marks[k], block) if k in marks else html  # noqa: E731
    logo = f'<div class="mw-logo"><span>{E(S["logo"])}</span><small>{E(S["logo_tools"])}</small></div>'
    side = [logo, M(f'<span class="mw-it{" on" if side_on in (None, S["new"]) and not hist_on else ""}">{S["new_icon"]} {E(S["new"])}</span>', "new")]
    for ic, lb in S["items"]:
        side.append(M(f'<span class="mw-it">{ic} {E(lb)}</span>', f"item:{lb}"))
    for title, entries in S["sections"]:
        side.append(M(f'<div class="mw-sec">{E(title)}</div>', f"sec:{title}", True))
        side += [f'<span class="mw-it">{E(e)}</span>' for e in entries]
    side.append(M(f'<div class="mw-sec">{E(S["hist_title"])}</div>', f'sec:{S["hist_title"]}', True))
    for h in hist:
        t = f'<span class="mw-it{" on" if h == hist_on else ""}">{E(h)}</span>'
        side.append(M(t, "hist") if h == hist_on else t)
    side.append(f'<div class="mw-prof">{E(S["profile"])}</div>')

    snd = M(f'<span class="snd">↑</span>', "send")
    if key == "gemini" and input_text is None:   # Gemini는 입력 전엔 🎙만 보이고 ↑는 글을 넣으면 나타남
        snd = ""
    ph_txt = input_text if input_text is not None else S["placeholder"]
    ph = f'<span class="ph">{"" if not paste else ""}{E(ph_txt)}</span>'
    if paste:
        ph = f'<span class="ph"><span class="mw-paste">📄 {E(paste)}</span>\n{E(ph_txt)}</span>'
    plus = M('<span class="plus">＋</span>', "plus")
    right = f'<span>{S["right_icons"]}</span>' if S["right_icons"] else ""
    if key == "claude":
        inbox = f'<div class="mw-in"><div class="r1">{M(ph, "input")}</div><div class="r2">{plus}{snd}</div></div>'
    else:
        inbox = f'<div class="mw-in">{plus}{M(ph, "input")}{right}{snd}</div>'
    if S["modes"]:
        modes = '<div class="mw-modes">' + "".join(f'<span class="{"on" if i == 0 else ""}">{E(m)}</span>' for i, m in enumerate(S["modes"])) + "</div>"
        inbox += M(modes, "mode", True)

    main = [f'<div class="mw-top">{E(S["topright"])}</div>']
    if not messages:
        main.append(f'<div class="mw-hello">{E(S["hello"])}</div>{inbox}<div style="flex:1"></div>')
    else:
        msgs = []
        for i, (who, text) in enumerate(messages):
            m = f'<div class="mw-msg {who}">{E(text)}</div>'
            msgs.append(mk(m, marks[i], block=True) if i in marks else m)
        if tools:
            t = "".join(M(f"<span>{E(x)}</span>", "copy") if x == S["copy_label"] else f"<span>{E(x)}</span>" for x in S["tools"])
            msgs.append(f'<div class="mw-tools">{t}</div>')
        main.append(f'<div class="mw-msgs">{"".join(msgs)}</div>{inbox}')
    if panel:
        title, body = panel
        main.append(f'<div class="mw-panel"><div class="pt"><span>{E(title)}</span>{M("<span>⧉ 복사</span>", "panelcopy")}</div>{E(body)}</div>')
    return (f'<div class="win-top"><span class="win-icon" style="background:{S["accent"]}"></span><span class="win-title">{E(S["url"])}</span></div>'
            f'<div class="mw mw-{key}"><div class="mw-side">{"".join(side)}</div><div class="mw-main">{"".join(main)}</div></div>')


def yt_block(url, title, icon):
    if url:
        vid = url.rstrip("/").split("/")[-1].split("v=")[-1].split("?")[0].split("&")[0]
        frame = (f'<div class="video"><iframe src="https://www.youtube-nocookie.com/embed/{E(vid)}" title="{E(title)}" '
                 'loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>')
        return ('<div class="vwrap">' + f'<p class="vcap">{icon} {E(title)}</p>' + frame
                + f'<p class="vlink">영상이 안 보이면 👉 <a href="{E(url)}" target="_blank" rel="noopener">유튜브에서 바로 보기</a></p></div>')
    return '<div class="vwrap"><div class="video"><div class="ph"><b>🎬 따라 하기 영상 준비 중</b>영상이 올라오면 이 자리에서 바로 볼 수 있습니다.</div></div></div>'


def video_block():
    """기존 홍보영상(유튜브)과 가이드 소개영상을 좌우로 나란히. 휴대폰에서는 위아래로."""
    return '<div class="vpair">' + yt_block(VIDEO_URL, VIDEO_TITLE, "🎬") + yt_block(GUIDE_VIDEO_URL, GUIDE_TITLE, "🧭") + '</div>'


# ───────────────────────── 모델별 안내 페이지 ─────────────────────────
MODEL_TIPS = {
    "gpt": dict(
        login="오른쪽 위 <b>로그인</b> → 구글·이메일 계정으로 들어갑니다(무료 계정 가능)",
        sidebar="왼쪽 메뉴가 안 보이면 왼쪽 위 ◫(사이드바 열기)를 누릅니다",
        paste_note="긴 프롬프트도 입력창에 그대로 들어갑니다. 입력창이 길어지면 스크롤해서 끝까지 들어갔는지만 확인하세요.",
        copy_note="답변 맨 아래 아이콘 줄의 첫 번째 ⧉(복사)를 누릅니다. 아이콘이 안 보이면 답변 위에 마우스를 올리세요.",
        result_note=None,
        stuck=[
            ["오른쪽 위 ◌(임시 채팅)이 켜져 있다", "임시 채팅은 대화가 '최근' 목록에 남지 않습니다. 4-3에서 돌아갈 수 없으니 꺼 두세요."],
            ["메모장에 ** 나 # 기호가 섞여 붙는다", "복사 버튼은 꾸밈 기호까지 복사합니다. \"메모장용 일반 글자로 다시 써 줘\"라고 보낸 뒤 다시 복사하세요."],
            ["\"한도에 도달했습니다\" 안내가 뜬다", "무료 사용량 제한입니다. 잠시 뒤 다시 하거나 Claude·Gemini 탭으로 옮겨 이어서 하세요(설명서 txt만 있으면 됩니다)."],
            ["답이 영어로 나온다", "\"한국어로 다시 써 줘\"라고 보내거나 새 채팅에서 다시 시작하세요."],
        ]),
    "claude": dict(
        login="<b>Google로 계속하기</b> 또는 이메일로 로그인합니다(무료 계정 가능). 처음 들어오면 뜨는 쿠키 안내는 원하는 쪽을 고르면 됩니다",
        sidebar="왼쪽 위 <b>Claude</b> 글자 옆 💬(채팅)·‹/›(코드) 중 <b>💬 채팅</b>이 선택되어 있어야 합니다. 메뉴가 안 보이면 맨 왼쪽 위 ▭(사이드바)를 누르세요",
        paste_note="Claude는 긴 글을 붙여넣으면 입력창 위에 <b>📄 붙여넣은 텍스트</b> 카드로 바꿔 붙입니다. 내용은 그대로 들어간 것이니 그냥 보내면 됩니다.",
        copy_note="답변 바로 아래 아이콘 줄의 ⧉(복사)를 누릅니다. 설명서가 화면 오른쪽 <b>문서 창</b>(아티팩트)에 따로 열렸다면, 그 창 오른쪽 위의 <b>복사</b>를 누르세요.",
        result_note="긴 설명서는 오른쪽에 문서 창으로 열릴 수 있습니다. 왼쪽 대화에는 요약 카드만 보여도 정상입니다.",
        stuck=[
            ["왼쪽에 '새 채팅' 버튼이 없다", "Claude는 <b>＋ 새로 만들기</b>가 '새 채팅'입니다. 교안의 '새 채팅'은 모두 이 버튼으로 읽으세요."],
            ["화면이 코드 편집 화면처럼 보인다", "왼쪽 위 Claude 글자 옆 ‹/›(코드)가 눌린 상태입니다. 💬(채팅)을 누르세요."],
            ["\"메시지 한도에 도달\" 안내가 뜬다", "무료 사용량 제한입니다. 안내된 시간 뒤에 다시 하거나 ChatGPT·Gemini 탭으로 옮겨 이어서 하세요."],
            ["붙여넣었는데 입력창에 글이 안 보인다", "입력창 위 📄 카드로 들어가 있습니다. 카드를 누르면 내용을 확인할 수 있습니다."],
        ]),
    "gemini": dict(
        login="구글 계정으로 로그인합니다(학교·회사 계정은 Gemini가 막혀 있을 수 있으니 <b>개인 구글 계정</b> 권장)",
        sidebar="입력창 아래 <b>채팅 / 작업</b> 중 <b>채팅</b>이 선택되어 있는지 확인합니다. 왼쪽 메뉴가 안 보이면 왼쪽 위 ◫를 누르세요",
        paste_note="긴 프롬프트도 입력창에 그대로 들어갑니다. 붙여넣으면 오른쪽 🎙 자리에 ↑(보내기)가 나타납니다.",
        copy_note="답변 아래 아이콘 줄(👍 👎 ↻ ⤴ ⧉ ⋮)에서 <b>⧉ 복사</b>를 누릅니다. 안 보이면 ⋮(더보기) 안에서 <b>복사</b>를 찾으세요.",
        result_note="긴 글은 오른쪽 <b>Canvas</b> 창에 열릴 수 있습니다. 그때는 Canvas 창 오른쪽 위의 ⧉(복사)를 누르세요.",
        stuck=[
            ["입력창 아래 '작업'이 선택되어 있다", "'작업'은 AI가 여러 단계를 스스로 진행하는 방식입니다. 오늘은 <b>채팅</b>을 누르고 시작하세요."],
            ["왼쪽에 지난 대화가 안 보인다", "왼쪽 위 🔍(검색)을 누르고 '마케팅' 등 대화 이름을 검색하세요."],
            ["\"Gemini를 사용할 수 없습니다\" 안내", "학교·회사 구글 계정의 제한입니다. 개인 구글 계정으로 다시 로그인하세요."],
            ["메모장에 ** 나 # 기호가 섞여 붙는다", "\"메모장용 일반 글자로 다시 써 줘\"라고 보낸 뒤 다시 복사하세요."],
        ]),
}


def model_page(key):
    S, T = MODELS[key], MODEL_TIPS[key]
    nm, new = S["name"], S["new"]
    NEW = ui(("＋ " if key == "claude" else "") + new)
    hist_all = ("스킬 실행 – 거치대", "스킬 실행 – 감귤잼", "마케팅 스킬 만들기")

    # ① 화면 둘러보기: 실제 화면 순서대로 번호
    rows, marks, n = [], {}, 0
    def add(mkey, name, where):
        nonlocal n
        n += 1
        marks[mkey] = n
        desc = S["item_desc"].get(name.replace(" ⌄", ""), "")
        used = name.replace(" ⌄", "") in S["today"] or mkey == "input"
        rows.append([str(n), name.replace(" ⌄", ""), where, desc or "프롬프트를 붙여넣는 곳", "✅ 사용" if used else "—"])
    add("new", new, "왼쪽 맨 위")
    for _, lb in S["items"]:
        add(f"item:{lb}", lb, "왼쪽 메뉴")
    for t, _ in S["sections"]:
        add(f"sec:{t}", t, "왼쪽 묶음")
    add(f'sec:{S["hist_title"]}', S["hist_title"], "왼쪽 아래 목록")
    add("input", "입력창 — " + S["placeholder"], "가운데")
    if S["modes"]:
        add("mode", "채팅 / 작업", "입력창 아래")
    marks_tour = dict(marks)
    tour_rows = [[r[0], r[1], r[2], r[3], r[4]] for r in rows]

    tour = (section(f"① {nm} 화면 둘러보기", f"실제 {nm} 첫 화면의 메뉴 순서 그대로 번호를 붙였습니다 (2026년 11월 화면 기준)")
            + figs(fig(f"{key}-00", f"{nm} 첫 화면 — 메뉴 순서", model_window(key, marks=marks_tour, hist=hist_all[2:])))
            + table(["번호", "메뉴(화면 표기)", "위치", "하는 일", "오늘"], tour_rows)
            + box("info", "오늘 쓰는 것은 딱 셋", f"<b>{E(new)}</b>(새 대화) · <b>입력창</b>(붙여넣기) · <b>{E(S['hist_title'].replace(' ⌄', ''))}</b>(지난 대화로 돌아가기). "
                  "나머지 메뉴는 눌러 보지 않아도 됩니다. 메뉴 이름·순서는 업데이트로 조금 바뀔 수 있습니다."))

    hist_name = S["hist_title"].replace(" ⌄", "")
    steps = [
        step("0", f"{nm} 열고 로그인하기", f"{nm} 첫 화면을 띄웁니다.",
             [f"크롬(Chrome) 주소창에 <b>{E(S['url'])}</b>를 입력하고 {kbd('Enter')}",
              T["login"], T["sidebar"],
              f"가운데에 <b>{E(S['hello'])}</b>와 입력창(<b>{E(S['placeholder'])}</b>)이 보이는지 확인합니다",
              f"메모장도 열어 둡니다({kbd('⊞ Windows')} → <b>메모장</b> 입력 → 열기)"],
             ok=f"위 '화면 둘러보기' 그림과 같은 화면이 보이면 성공입니다.",
             stuck="로그인 화면에서 막히면 이미 쓰는 다른 AI 탭으로 바꿔 진행해도 됩니다. 결과는 같습니다.", one=True),
        step("1", "맛보기 — 한 줄 부탁 vs 설명서 부탁 (선택)", "정보 없이 부탁하면 AI가 무엇을 지어내는지 비교해 봅니다. 시간이 없으면 건너뛰세요.",
             [f"왼쪽 위 {NEW}을 누릅니다",
              f"아래 첫 번째 상자를 {ui('복사')} → 입력창에 {kbd('Ctrl', 'V')} → {kbd('Enter')}",
              f"결과를 본 뒤, 같은 대화에서 두 번째 상자를 {ui('복사')} → 붙여넣기 → 보내기"],
             extra=prompt(P_TASTE_1) + prompt(P_TASTE_2),
             ok="첫 번째 결과에는 알려 주지 않은 가격·'1위' 같은 말이 섞일 수 있고, 두 번째는 형식대로 나오며 가격은 [확인 필요]로 표시됩니다.",
             figure=fig(f"{key}-01", f"{new} → 붙여넣기 → 보내기", model_window(
                 key, marks={"new": 1, "input": 2, "send": 3}, input_text=P_TASTE_1, hist=hist_all[2:]))),
        step("2-1", "만들 콘텐츠 3개 고르기", "내 스킬이 만들 콘텐츠를 정합니다.",
             ["아래에서 <b>3개</b>를 고릅니다: 인스타그램 게시글 · 네이버 블로그 글 · 카카오톡 채널 홍보 메시지 · 상세페이지 소개 문구 · 숏폼 영상 대본(30초) · 홍보 이메일 · 문자(SMS) 문구",
              "(선택) 내 스킬만의 특징 1개: 대상별 말투 / 제목 후보 2개 / 이미지 아이디어 / 확인 필요 목록"],
             ok="고른 3개를 메모해 두었으면 다음으로 갑니다. 고르기 어렵다면 프롬프트에 이미 적힌 3개를 그대로 쓰세요.", one=True),
        step("2-2", "스킬 만드는 프롬프트 보내기", "과제 조건에 맞는 스킬 설명서 초안을 받습니다.",
             [f"왼쪽 위 {NEW}을 누릅니다",
              f"아래 상자의 {ui('복사')} → 입력창 클릭 → {kbd('Ctrl', 'V')}",
              "<b>[내가 만들고 싶은 콘텐츠]</b>·<b>[내 스킬만의 특징]</b> 아래 줄만 내 것으로 바꿉니다(입력창 안에서 고치기 어려우면 그대로 보내도 됩니다)",
              f"오른쪽 {ui('↑')}(보내기)를 누릅니다"],
             extra=prompt(P_MAKE) + box("info", f"{nm}에서는", T["paste_note"]),
             ok="'0. 스킬 이름과 한 줄 설명' ~ '5. 최종 출력 순서'까지 번호 붙은 설명서가 나오면 성공입니다.",
             stuck=f"답이 끊기면 \"계속\", 표·** 기호가 섞이면 \"메모장용 일반 글자로 다시 써 줘\". 줄 바꿈은 {kbd('Shift', 'Enter')}입니다.",
             figure=figs(
                 fig(f"{key}-02", "새 대화 → 프롬프트 붙여넣기 → 보내기", model_window(
                     key, marks={"new": 1, "input": 2, "send": 4},
                     input_text="" if key == "claude" else "너는 마케팅 업무를 돕는 'AI 스킬'을 설계하는 전문가야. …",
                     paste="붙여넣은 텍스트 · 31줄" if key == "claude" else None, hist=("감귤잼 홍보 글",))),
                 fig(f"{key}-03", "AI가 만든 스킬 설명서(예시)", model_window(
                     key, [("user", "너는 마케팅 업무를 돕는 'AI 스킬'을 설계하는 전문가야. …"),
                           ("ai", "스킬 설명서를 만들었습니다." if key == "claude" else skill_preview())],
                     hist=("마케팅 스킬 만들기", "감귤잼 홍보 글"), hist_on="마케팅 스킬 만들기",
                     panel=("📄 스킬 설명서", skill_preview()) if key == "claude" else None)))),
        step("2-3", "복사해서 메모장에 txt로 저장", "제출할 스킬 파일을 만듭니다.",
             [T["copy_note"],
              f"메모장 클릭 → {kbd('Ctrl', 'V')}",
              f"{ui('파일')} → {ui('다른 이름으로 저장')}",
              f"파일 이름 <b>트랙B_스킬_내이름.txt</b>, 인코딩 {ui('UTF-8')} 확인 → {ui('저장')}"],
             ok="메모장 제목이 '트랙B_스킬_내이름.txt - 메모장'으로 바뀌면 성공입니다.",
             stuck=f"복사 아이콘을 못 찾으면 답변 글을 마우스로 끌어 선택 → {kbd('Ctrl', 'C')}.",
             figure=figs(
                 fig(f"{key}-04", f"{nm} 답변 아래 복사 버튼" + (" (문서 창이면 창 위 복사)" if key == "claude" else ""), model_window(
                     key, [("user", "너는 마케팅 업무를 돕는 'AI 스킬'을 설계하는 전문가야. …"),
                           ("ai", "스킬 설명서를 만들었습니다." if key == "claude" else skill_preview())],
                     tools=True, marks={"copy": 1, "panelcopy": 1} if key == "claude" else {"copy": 1},
                     panel=("📄 스킬 설명서", skill_preview()) if key == "claude" else None,
                     hist=("마케팅 스킬 만들기",), hist_on="마케팅 스킬 만들기")),
                 fig(f"{key}-05", "메모장 → 다른 이름으로 저장 → UTF-8", notepad(
                     skill_preview(), text_mark=2, overlay=save_dialog("트랙B_스킬_내이름.txt", n_name=4, n_enc=None))))),
        step("3-1", "새 대화에 스킬 설명서 넣기", "처음 보는 AI도 내 설명서만으로 일하는지 시험합니다.",
             [f"{NEW}을 누릅니다",
              f"아래 시작 문장을 {ui('복사')} → 입력창에 {kbd('Ctrl', 'V')}",
              f"메모장에서 {kbd('Ctrl', 'A')} → {kbd('Ctrl', 'C')} → 입력창(시작 문장 아래)에 {kbd('Ctrl', 'V')}",
              f"{ui('↑')}(보내기)"],
             extra=prompt(P_RUN),
             ok="AI가 \"상품 정보를 보내 주세요\"라고 답하면 성공입니다.",
             stuck=f"{ui('＋')}(파일 추가)로 txt 파일을 올리고 시작 문장만 보내도 됩니다." + (" 붙여넣은 설명서가 📄 카드로 바뀌는 것은 정상입니다." if key == "claude" else ""),
             figure=fig(f"{key}-06", "새 대화 → 시작 문장 + 설명서 → 보내기", model_window(
                 key, marks={"new": 1, "input": 3, "send": 4},
                 input_text="지금부터 붙여넣는 글은 '스킬 설명서'야. …" + ("" if key == "claude" else "\n\n0. 스킬 이름과 한 줄 설명 …"),
                 paste="붙여넣은 텍스트 · 스킬 설명서" if key == "claude" else None, hist=("마케팅 스킬 만들기",)))),
        step("3-2", "샘플 상품(감귤잼) 보내기", "스킬을 실제로 돌려 샘플 출력물을 만듭니다.",
             [f"같은 대화에서 아래 상자를 {ui('복사')} → 붙여넣기 → 보내기"],
             extra=prompt(SAMPLE1),
             ok="정한 콘텐츠가 순서대로 나오고 가격 자리에 [확인 필요]가 보이면 성공입니다." + (f" {T['result_note']}" if T["result_note"] else ""),
             stuck=f"AI가 가격을 먼저 물으면 정상입니다. 아래를 보내세요.{prompt(P_NO_PRICE)}",
             figure=fig(f"{key}-07", "콘텐츠가 한 번에 나옴(예시)", model_window(
                 key, [("user", "[상품 정보] ※ 실습용 가상 상품입니다\n- 상품명: 귤빛담은 수제 감귤잼 …"),
                       ("ai", "[1] 인스타그램 게시글\n아이 간식, 성분표부터 보게 되시죠? …\n\n[2] 네이버 블로그 글\n제목: …\n\n[3] 카카오톡 채널 메시지 …\n\n※ 가격: [확인 필요]")],
                 tools=True, marks={"copy": 1}, hist=("스킬 실행 – 감귤잼", "마케팅 스킬 만들기"), hist_on="스킬 실행 – 감귤잼"))),
        step("3-3", "출력물 저장", "심사 보조자료(샘플 출력물)를 파일로 남깁니다.",
             [f"답변 아래 {ui('⧉ 복사')}",
              f"메모장 {kbd('Ctrl', 'N')}(새 탭) → {kbd('Ctrl', 'V')}",
              f"{ui('파일')} → {ui('다른 이름으로 저장')} → <b>트랙B_출력물_감귤잼_내이름.txt</b>"],
             ok="메모장 위에 탭 두 개(스킬, 출력물)가 보이면 성공입니다.", one=True),
        step("4-1", "결과물 점검시키기", "지어낸 내용·형식 위반을 AI가 스스로 찾게 합니다.",
             [f"3-2를 한 <b>같은 대화</b>에서 아래 상자를 {ui('복사')} → 붙여넣기 → 보내기"],
             extra=prompt(P_CHECK),
             ok="1번·3번이 모두 \"없음\"이면 통과. 문제가 있었다면 4번의 고친 결과로 출력물 파일을 바꿔 저장하세요.", one=True),
        step("4-2", "다른 상품(노트북 거치대)으로 재사용 시험", "필수 ③ — 다른 상품에도 되는지 확인합니다.",
             [f"{NEW} → 3-1처럼 시작 문장 + 설명서 보내기",
              f"아래 상자를 {ui('복사')} → 붙여넣기 → 보내기"],
             extra=prompt(SAMPLE2),
             ok="감귤잼 때와 같은 구성·순서로 거치대에 맞는 내용이 나오면 성공입니다.",
             stuck="'감귤', '아이 간식' 이야기가 섞이면 설명서에 특정 상품이 남아 있다는 뜻입니다. 4-3에서 고치세요.", one=True),
        step("4-3", "스킬 설명서 고치기", f"왼쪽 '{hist_name}' 목록에서 스킬을 만든 대화로 돌아가 고칩니다.",
             [f"왼쪽 <b>{E(hist_name)}</b> 목록에서 {ui('마케팅 스킬 만들기')}(스킬을 만든 대화)를 누릅니다",
              f"아래 상자를 {ui('복사')} → 붙여넣기 → <b>[문제]</b> 아래 줄을 내가 겪은 문제로 바꾸기",
              "보내기",
              f"새 설명서를 {ui('⧉ 복사')} → 메모장 스킬 탭 {kbd('Ctrl', 'A')} → {kbd('Ctrl', 'V')} → {kbd('Ctrl', 'S')}"],
             extra=prompt(P_FIX),
             ok="고친 설명서로 3-1~3-2를 새 대화에서 다시 돌려 문제가 사라지면 성공입니다.",
             stuck=f"대화 이름은 {nm}가 자동으로 붙여서 다를 수 있습니다. 목록에서 찾기 어려우면 🔍 검색에 '스킬'을 입력하세요.",
             figure=fig(f"{key}-08", f"'{hist_name}' 목록 → 스킬 만든 대화 → 고치기 요청", model_window(
                 key, [("ai", "스킬 설명서를 만들었습니다." if key == "claude" else skill_preview())],
                 hist=hist_all, hist_on="마케팅 스킬 만들기", input_text="스킬 설명서를 시험해 봤더니 아래 문제가 있었어. …",
                 marks={"hist": 1, "input": 2, "send": 3}))),
        step("5", "최종 점검과 제출 파일 정리", "과제 조건 5개를 모두 채웠는지 확인합니다.",
             [f"{NEW} → 아래 상자를 {ui('복사')} → 붙여넣기",
              f"이어서 메모장 스킬 설명서 전체({kbd('Ctrl', 'A')} → {kbd('Ctrl', 'C')})를 입력창 끝에 {kbd('Ctrl', 'V')} → 보내기",
              "'부족'이 나온 조건은 알려 준 문장을 설명서에 넣고 저장",
              f"<a href='#p5' data-go='p5'>5 제출 탭</a>의 점검표로 파일 2개(스킬 txt · 출력물 txt)를 확인"],
             extra=prompt(P_FINAL),
             ok="다섯 조건이 모두 '충족'이고 파일 2개가 준비되면 끝입니다. 수고하셨습니다! 🎉", one=True),
    ]
    html = "".join(steps)
    for st in ["0", "1", "2-1", "2-2", "2-3", "3-1", "3-2", "3-3", "4-1", "4-2", "4-3", "5"]:
        html = html.replace(f'id="s{st}"', f'id="{key}-s{st}"', 1)
    trouble = (section(f"③ {nm}에서 자주 막히는 점")
               + table(["이런 일이 생기면", "이렇게 하세요"], T["stuck"], raw=True)
               + box("info", "다른 AI로 옮겨도 됩니다", "스킬 설명서 txt 파일만 있으면 ChatGPT·Claude·Gemini 어디서든 3-1부터 이어서 할 수 있습니다."))
    other = " · ".join(f"<a href='#{k}' data-go='{k}'>{MODELS[k]['icon']} {MODELS[k]['name']}</a>" for k in MODELS if k != key)
    return wrap(
        tab_hero(S["icon"], f"{nm} 사용자용 · 처음부터 끝까지 한 페이지", f"{nm}로 따라 하기",
                 f"{nm} 실제 화면의 메뉴 이름과 순서대로 안내합니다")
        + box("info", "이 페이지만 보면 됩니다", f"준비부터 제출까지 {nm} 화면 기준으로 한 페이지에 모았습니다. "
              f"단계별 자세한 설명은 0~5 탭에 있습니다. 다른 AI를 쓴다면 👉 {other}")
        + tour + section(f"② {nm}로 따라 하기", "번호 순서대로 — 글의 번호와 그림의 빨간 번호가 같은 곳을 가리킵니다") + html + trouble,
        pc_note=PC)


def model_pager(key):
    ks = list(MODELS)
    other = "".join(f'<a class="prev" href="#{k}" data-go="{k}"><small>다른 AI로 보기</small><b>{MODELS[k]["icon"]} {E(MODELS[k]["name"])}</b></a>'
                    for k in ks if k != key)
    return (f'<nav class="pager" aria-label="단계 이동"><a class="prev" href="#home" data-go="home"><small>← 처음으로</small><b>홈 · AI 다시 고르기</b></a>'
            f'<a class="next" href="#ap" data-go="ap"><small>막히면 →</small><b>부록</b></a></nav>'
            f'<nav class="pager" aria-label="다른 AI">{other}</nav>')


def pick_cards():
    desc = {"gpt": "OpenAI의 AI. 왼쪽 메뉴: 새 채팅 · 이미지 · 예약 · 라이브러리 …",
            "claude": "Anthropic의 AI. 왼쪽 메뉴: 새로 만들기 · 검색 · 프로젝트 · 아티팩트 …",
            "gemini": "Google의 AI. 왼쪽 메뉴: 새 채팅 · 라이브러리 · 이미지 · 예약 …"}
    return '<div class="pick">' + "".join(
        f'<a href="#{k}" data-go="{k}" style="border-color:{S["accent"]}33"><span style="font-size:26px">{S["icon"]}</span>'
        f'<b>{E(S["name"])}</b><small>{E(S["url"])}<br>{E(desc[k])}</small><span class="go" style="color:{S["accent"]}">{E(S["name"])} 화면으로 따라 하기 →</span></a>'
        for k, S in MODELS.items()) + "</div>"


# ───────────────────────── 홈 ─────────────────────────
home = clay_hero("제5회 2026 스마트워크톤 · 트랙B", "스킬 제작 가이드<br><em>복사·붙여넣기로<br>완성하는 AI 스킬</em>",
            "AI를 잘 몰라도 괜찮습니다. 화면 순서대로 복사하고 붙여넣기만 하면, 상품 정보 하나로 마케팅 콘텐츠를 한 번에 만드는 나만의 AI 스킬이 완성됩니다.",
            ["📋 복사·붙여넣기", "🤖 ChatGPT·Claude·Gemini", "📄 txt 제출", "⏱ 약 90분"]) + wrap(
    section("내가 쓰는 AI를 고르세요", "고른 AI의 실제 화면(메뉴 이름·순서) 그대로 처음부터 끝까지 따라 하는 페이지로 이동합니다")
    + pick_cards()
    + section("시작하기 전에, 이 영상 먼저", "AI가 낯설어도, 대회가 처음이어도 괜찮습니다 — 두 영상이면 마음이 한결 가벼워집니다")
    + video_block()
    + section("오늘의 과제", "개인전 과제를 그대로 따라갑니다")
    + table(["항목", "내용"], [
        ["과제", "상품 정보를 넣으면 여러 마케팅 콘텐츠를 한 번에 만들어 내는, 다시 쓸 수 있는 AI 스킬 만들기"],
        ["필수 ①", "상품 특징과 홍보 대상을 입력받아 반영할 것"],
        ["필수 ②", "콘텐츠별 제작 절차와 출력 형식을 명시할 것"],
        ["필수 ③", "다른 상품에도 다시 쓸 수 있게 구성할 것"],
        ["제약", "제공되지 않은 성능·가격을 지어내지 않기 / 시험용으로만 생성, 실제 게시·유료 결제 금지"],
        ["제출", "스킬 txt 파일 + 샘플 상품으로 실행한 출력물(심사 보조자료)"],
    ])
    + box("info", "스킬이 뭔가요?", "AI에게 주는 <b>'업무 설명서'</b>입니다. 신입 직원에게 업무 매뉴얼을 건네듯, 설명서를 AI에게 붙여넣으면 매번 같은 방식·같은 품질로 일합니다. 오늘은 이 설명서를 txt 파일로 만듭니다.")
    + section("오늘 만드는 것")
    + cards([("📄", "스킬 설명서 (txt)", "어떤 상품이든 넣으면 콘텐츠 3종 이상을 만들어 주는 설명서"),
             ("📝", "샘플 출력물", "가상 상품으로 실제 실행해 본 결과 — 심사 보조자료"),
             ("🔁", "재사용 시험", "다른 상품으로도 잘 되는지 확인하고 고치기")], cols=3)
    + section("진행 순서", "탭을 왼쪽부터 차례로 누르며 따라 하세요")
    + flow([("0. 준비", "AI·메모장 열기"), ("1. 맛보기", "스킬이 왜 필요한지"), ("2. 만들기", "프롬프트 1번이면 초안"),
            ("3. 실행", "새 채팅에서 돌려 보기"), ("4. 점검", "지어낸 말·재사용 확인"), ("5. 제출", "파일 2개 정리")])
    + table(["탭", "하는 일", "시간(예상)"], [
        ["0 준비", "AI 채팅과 메모장 열기", "약 10분"], ["1 맛보기", "한 줄 부탁 vs 설명서 부탁 비교", "약 10분"],
        ["2 만들기", "콘텐츠 고르기 → 스킬 만드는 프롬프트 → 메모장 저장", "약 25분"],
        ["3 실행", "새 채팅에 스킬 넣고 샘플 상품으로 실행 → 결과 저장", "약 15분"],
        ["4 점검", "지어낸 내용 점검 → 다른 상품으로 시험 → 고치기", "약 20분"],
        ["5 제출", "최종 점검표 확인, 제출 파일 정리", "약 10분"]])
    + section("꼭 지킬 원칙 3가지")
    + box("no", "① 지어내지 않기", "내가 준 정보에 없는 가격·성능·후기는 쓰지 않습니다. 모르면 <b>[확인 필요]</b>로 둡니다. (심사에서 가장 먼저 보는 부분입니다)")
    + box("warn", "② 시험용으로만", "만든 콘텐츠를 실제 SNS에 올리거나 광고비·유료 결제를 하지 마세요.")
    + box("ok", "③ 개인정보·회사 자료 넣지 않기", "고객 이름·연락처, 회사 내부 문서는 AI에 붙여넣지 않습니다. 실습은 가상 상품으로 합니다.")
    + section("실습 파일", "필요할 때 내려받으세요(각 단계의 복사 버튼만으로도 충분합니다)")
    + downloads([("practice/prompts_all.txt", "📋 오늘 쓰는 프롬프트 모음", "g"),
                 ("practice/sample_product_1.txt", "🍊 샘플 상품 1 (감귤잼)", ""),
                 ("practice/sample_product_2.txt", "💻 샘플 상품 2 (노트북 거치대)", ""),
                 ("practice/product_form.txt", "✍ 내 상품 정보 입력 틀", ""),
                 ("practice/skill_template.txt", "🧩 스킬 설명서 빈칸 틀", ""),
                 ("practice/checklist.txt", "✅ 제출 전 점검표", "")])
    + box("info", "그림 안내", "교안의 화면 그림은 이해를 돕는 <b>모형</b>입니다. ChatGPT·Claude·Gemini 어느 것을 써도 '새 채팅 → 붙여넣기 → 보내기' 순서는 같습니다(Claude는 '새 채팅' 대신 '＋ 새로 만들기'). 내 AI의 실제 화면 배치로 보고 싶다면 위 <b>AI 고르기</b>에서 고르세요. 글의 번호와 그림의 빨간 번호가 같은 곳을 가리킵니다."))

# ───────────────────────── 0 준비 ─────────────────────────
p0 = wrap("".join([
    tab_hero("🧰", "STEP 0 · 약 10분", "준비", "AI 채팅 창과 메모장, 두 개만 열면 됩니다"),
    step("0-1", "AI 채팅 열기", "스킬을 만들고 시험할 AI 채팅 창을 엽니다.",
         ["크롬(Chrome)을 열고 아래 표의 주소 중 하나로 들어가 로그인합니다",
          f"왼쪽 위 {ui('＋ 새 채팅')}을 누릅니다",
          "화면 아래 입력창이 보이는지 확인합니다"],
         extra=table(["AI", "주소", "새 대화 버튼"], [["ChatGPT", "chatgpt.com", "새 채팅"], ["Claude", "claude.ai", "＋ 새로 만들기"],
                                                   ["Gemini", "gemini.google.com", "새 채팅"]])
         + box("info", "어떤 AI든 괜찮아요", "무료 계정으로도 오늘 실습을 모두 할 수 있습니다. 이미 쓰고 있는 AI가 있다면 그것을 쓰세요. "
               "이 교안의 '새 채팅'은 Claude에서는 <b>＋ 새로 만들기</b>입니다. 내 AI 화면 그대로 보려면 위쪽 "
               "<a href='#gpt' data-go='gpt'>🟢 ChatGPT</a> · <a href='#claude' data-go='claude'>🟠 Claude</a> · <a href='#gemini' data-go='gemini'>🔵 Gemini</a> 탭을 보세요."),
         ok="가운데에 인사말, 아래에 '메시지를 입력하세요' 입력창이 보이면 성공입니다.",
         stuck=f"로그인 화면이 나오면 {ui('Google로 계속하기')}를 눌러 구글 계정으로 들어가면 가장 빠릅니다.",
         figure=fig("m0-01", "＋ 새 채팅 → 입력창", ai_window(new_mark=2, hist=(), marks={"input": 3}))),
    step("0-2", "메모장 열기", "완성한 스킬을 txt 파일로 저장할 메모장을 엽니다.",
         [f"키보드의 {kbd('⊞ Windows')} 키를 누르고 <b>메모장</b>을 입력합니다",
          f"검색 결과의 {ui('메모장')}을 누릅니다"],
         ok="하얀 빈 메모장 창이 열리면 성공입니다. AI 창과 메모장을 나란히 띄워 두면 편합니다.",
         stuck=f"맥(Mac)은 {ui('텍스트 편집기')}(TextEdit)를 열고 메뉴 {ui('포맷')} → {ui('일반 텍스트로 만들기')}를 먼저 누르세요.",
         figure=fig("m0-02", "Windows 검색 → 메모장", '<div class="ws">' + mk('<div class="q">🔍 메모장</div>', 1, block=True)
                    + '<div class="lbl">가장 일치하는 항목</div>'
                    + mk('<div class="res"><span class="ico"></span><span><b>메모장</b><br><small>앱</small></span></div>', 2, block=True) + "</div>")),
]), pc_note=PC)

# ───────────────────────── 1 맛보기 ─────────────────────────
p1 = wrap("".join([
    tab_hero("🍊", "STEP 1 · 약 10분", "맛보기 — 스킬이 왜 필요할까?", "한 줄 부탁과 설명서 부탁을 비교합니다"),
    step("1-1", "한 줄로만 부탁해 보기", "정보 없이 부탁하면 AI가 무엇을 지어내는지 직접 봅니다.",
         [f"아래 문장의 {ui('복사')}를 누릅니다",
          f"AI 입력창을 누르고 {kbd('Ctrl', 'V')}로 붙여넣습니다",
          f"{ui('↑')}(보내기)를 누르거나 {kbd('Enter')}를 누릅니다"],
         extra=prompt(P_TASTE_1),
         ok="그럴듯한 홍보 글이 나옵니다. 그런데 잘 보면 <b>우리가 알려주지 않은 가격, '최고', '1위' 같은 말</b>이 섞여 있을 수 있습니다. 이것이 심사에서 감점되는 '지어낸 정보'입니다.",
         figure=figs(fig("m1-01", "붙여넣기 → 보내기", ai_window(input_text=P_TASTE_1, marks={"input": 2, "send": 3}, hist=())),
                     fig("m1-02", "결과 예시 — 주지 않은 정보가 섞임", ai_window(
                         [("user", P_TASTE_1), ("ai", "🍊 제주의 햇살을 담은 최고의 감귤잼!\n지금 단 9,900원에 만나보세요.\n고객 만족도 1위 …")], hist=())))),
    step("1-2", "정보와 형식을 주고 부탁해 보기", "상품 정보·만드는 방법·출력 형식을 주면 결과가 어떻게 달라지는지 봅니다.",
         [f"같은 채팅에서 아래 상자의 {ui('복사')}를 누릅니다",
          f"입력창에 {kbd('Ctrl', 'V')} 후 보내기"],
         extra=prompt(P_TASTE_2),
         ok="첫 문장 + 짧은 본문 + 해시태그 5개 형식으로 나오고, 가격은 쓰지 않거나 [확인 필요]로 표시됩니다.",
         stuck="결과가 형식과 조금 다르면 \"출력 형식을 정확히 지켜서 다시 써 줘\"라고 보내세요.",
         figure=fig("m1-03", "설명을 붙여 부탁한 결과", ai_window(
             [("user", "아래 상품으로 인스타그램 게시글을 만들어 줘.\n[상품 정보] …\n[만드는 방법] …\n[출력 형식] …"),
              ("ai", "아이 간식, 성분표부터 보게 되시죠?\n제주 감귤과 비정제 원당으로 만든 잼이에요.\n보존료·색소는 넣지 않았어요. …\n#감귤잼 #아이간식 #제주감귤 #수제잼 #아침메뉴")],
             marks={"input": 2}, hist=()))),
    box("ok", "여기까지 배운 것",
        "설명(정보·방법·형식·규칙)을 주면 결과가 좋아집니다. 하지만 매번 이렇게 길게 쓰기는 번거롭죠. "
        "<b>이 설명을 상품에 상관없이 쓸 수 있게 정리해 파일로 저장해 둔 것이 바로 '스킬'</b>입니다. 다음 탭에서 AI에게 그 설명서를 만들게 합니다."),
]), pc_note=PC)

# ───────────────────────── 2 만들기 ─────────────────────────
p2 = wrap("".join([
    tab_hero("🧩", "STEP 2 · 약 25분", "스킬 만들기", "프롬프트 한 번으로 초안을 받고 메모장에 저장합니다"),
    flow([("콘텐츠 고르기", "3개 추천"), ("만드는 프롬프트", "[ ] 두 곳만 고치기"), ("메모장 저장", "txt 파일 완성")]),
    step("2-1", "만들 콘텐츠와 내 스킬의 특징 정하기", "어떤 콘텐츠를 만들지 고릅니다. 여기서 고른 것이 나만의 스킬이 됩니다.",
         ["아래 표에서 만들고 싶은 콘텐츠를 <b>3개</b> 고릅니다(처음이면 3개가 가장 안정적입니다)",
          "'내 스킬만의 특징'을 하나 골라도 좋습니다(없으면 그냥 두세요)"],
         extra=table(["콘텐츠", "이럴 때 좋아요"], [
             ["인스타그램 게시글", "짧고 감성적인 소개 + 해시태그"], ["네이버 블로그 글", "검색으로 찾아오는 사람에게 자세한 소개"],
             ["카카오톡 채널 홍보 메시지", "이미 아는 고객에게 짧은 소식"], ["상세페이지 소개 문구", "쇼핑몰 상품 페이지 위쪽 문구"],
             ["숏폼 영상 대본(30초)", "릴스·쇼츠용 장면별 대사"], ["홍보 이메일", "거래처·단골에게 보내는 안내"], ["문자(SMS) 문구", "90자 안쪽 짧은 안내"]])
         + table(["내 스킬만의 특징(예시)", "이렇게 적으면 됩니다"], [
             ["홍보 대상별 말투", "홍보 대상의 나이와 상황에 맞게 말투를 바꾼다"],
             ["제목 후보", "콘텐츠마다 제목 후보를 2개씩 제안한다"],
             ["이미지 아이디어", "콘텐츠마다 어울리는 사진·그림 아이디어를 한 줄 붙인다"],
             ["확인 필요 목록", "마지막에 [확인 필요]로 표시한 항목을 모아서 보여 준다"]]),
         ok="고른 콘텐츠 3개와(선택) 특징 1개를 메모해 두었으면 다음 단계로 갑니다.", one=True),
    step("2-2", "스킬 만드는 프롬프트 보내기", "AI에게 과제 조건에 맞는 스킬 설명서 초안을 만들게 합니다.",
         [f"AI 화면 왼쪽 위 {ui('＋ 새 채팅')}을 누릅니다",
          f"아래 상자의 {ui('복사')}를 누릅니다",
          f"입력창에 {kbd('Ctrl', 'V')}로 붙여넣고, <b>[내가 만들고 싶은 콘텐츠]</b> 아래 줄과 <b>[내 스킬만의 특징]</b> 아래 줄만 2-1에서 고른 것으로 바꿉니다",
          f"{ui('↑')}(보내기)를 누릅니다"],
         extra=prompt(P_MAKE)
         + box("info", "고치는 곳은 딱 두 줄", "예) 인스타그램 게시글, 숏폼 영상 대본(30초), 문자(SMS) 문구 / 특징: 콘텐츠마다 제목 후보를 2개씩 제안한다. 나머지는 그대로 두세요 — 과제 조건이 이미 들어 있습니다."),
         ok="'0. 스킬 이름과 한 줄 설명'부터 '5. 최종 출력 순서'까지 번호가 붙은 설명서가 나오면 성공입니다.",
         stuck=f"표나 ** 기호가 섞여 나오면 \"메모장용 일반 글자로 다시 써 줘\"라고 보내세요. 답이 중간에 끊기면 \"계속\"이라고 보내세요. 입력창에서 줄을 바꾸려면 {kbd('Shift', 'Enter')}입니다.",
         figure=figs(fig("m2-01", "새 채팅 → 붙여넣기 → 보내기", ai_window(
             new_mark=1, input_text="너는 마케팅 업무를 돕는 'AI 스킬'을 설계하는 전문가야. …", marks={"input": 3, "send": 4}, hist=("감귤잼 홍보 글",))),
             fig("m2-02", "AI가 만든 스킬 설명서 초안(예시)", ai_window(
                 [("user", "너는 마케팅 업무를 돕는 'AI 스킬'을 설계하는 전문가야. …"), ("ai", skill_preview())],
                 hist=("마케팅 스킬 만들기", "감귤잼 홍보 글"), hist_on="마케팅 스킬 만들기")))),
    step("2-3", "메모장에 붙여넣고 txt로 저장하기", "AI가 만든 설명서를 내 컴퓨터에 txt 파일로 저장합니다. 이것이 제출할 스킬 파일입니다.",
         [f"AI 답변 바로 아래의 {ui('⧉ 복사')} 아이콘을 누릅니다",
          f"메모장을 누르고 {kbd('Ctrl', 'V')}로 붙여넣습니다",
          f"메뉴 {ui('파일')} → {ui('다른 이름으로 저장')}을 누릅니다",
          f"파일 이름에 <b>트랙B_스킬_내이름.txt</b>를 입력하고, 인코딩이 {ui('UTF-8')}인지 확인한 뒤 {ui('저장')}을 누릅니다"],
         ok="메모장 맨 위 제목이 '트랙B_스킬_내이름.txt - 메모장'으로 바뀌면 성공입니다. 저장 위치(보통 '문서' 폴더)를 기억해 두세요.",
         stuck=f"복사 아이콘이 안 보이면 답변 위에 마우스를 올려 보세요. 그래도 없으면 답변 글을 마우스로 끌어 선택한 뒤 {kbd('Ctrl', 'C')}. "
               f"맥 텍스트 편집기는 {ui('파일')} → {ui('저장')}에서 '일반 텍스트 인코딩: 유니코드(UTF-8)'를 고르세요.",
         figure=figs(fig("m2-03", "답변 아래 복사 아이콘", ai_window([("ai", skill_preview())], tools_mark=1,
                                                                      hist=("마케팅 스킬 만들기",), hist_on="마케팅 스킬 만들기")),
                     fig("m2-04", "메모장에 붙여넣기 → 파일 → 다른 이름으로 저장", notepad(
                         skill_preview(), text_mark=2, marks={"파일": None}, dd_for=("파일", dropdown(NP_FILE_MENU, width=170)))),
                     fig("m2-05", "파일 이름 입력, 인코딩 UTF-8 → 저장", notepad(
                         skill_preview(), overlay=save_dialog("트랙B_스킬_내이름.txt", n_name=4, n_enc=None, n_save=None))))),
]), pc_note=PC)

# ───────────────────────── 3 실행 ─────────────────────────
p3 = wrap("".join([
    tab_hero("🚀", "STEP 3 · 약 15분", "스킬 실행해 보기", "심사위원처럼 '처음 보는 AI'에게 스킬을 줘 봅니다"),
    box("info", "왜 새 채팅에서 하나요?", "스킬을 만든 대화에는 이미 많은 설명이 쌓여 있어서, 설명서가 부족해도 AI가 눈치로 채워 줍니다. "
        "<b>새 채팅</b>에서 설명서만 주고도 잘 돌아가야 진짜 '다시 쓸 수 있는 스킬'입니다."),
    step("3-1", "새 채팅에 스킬 설명서 넣기", "아무것도 모르는 새 채팅에 내 스킬을 알려 줍니다.",
         [f"{ui('＋ 새 채팅')}을 누릅니다",
          f"아래 시작 문장을 {ui('복사')}해 입력창에 {kbd('Ctrl', 'V')}로 붙여넣습니다",
          f"{kbd('Shift', 'Enter')}를 두 번 눌러 줄을 띄웁니다",
          f"메모장에서 {kbd('Ctrl', 'A')}(전체 선택) → {kbd('Ctrl', 'C')}(복사) 후, 입력창에 다시 {kbd('Ctrl', 'V')}",
          f"{ui('↑')}(보내기)를 누릅니다"],
         extra=prompt(P_RUN),
         ok="AI가 \"상품 정보를 보내 주세요\"라고 답하면 성공입니다.",
         stuck="AI가 바로 콘텐츠를 만들어 버리면 괜찮습니다. 다음 단계로 상품 정보를 보내면 됩니다. "
               "입력창에 붙여넣기 대신 📎(파일 첨부)로 txt 파일을 올리고 시작 문장만 보내도 됩니다.",
         figure=fig("m3-01", "새 채팅 → 시작 문장 + 설명서 붙여넣기 → 보내기", ai_window(
             new_mark=1, input_text="지금부터 붙여넣는 글은 '스킬 설명서'야. …\n\n0. 스킬 이름과 한 줄 설명 …",
             marks={"input": 2, "send": 5}, hist=("마케팅 스킬 만들기",)))),
    step("3-2", "샘플 상품 정보 보내기", "가상 상품 '감귤잼' 정보로 스킬을 실제로 돌려 봅니다.",
         [f"아래 상자의 {ui('복사')}를 누릅니다",
          f"같은 채팅 입력창에 {kbd('Ctrl', 'V')} 후 보내기"],
         extra=prompt(SAMPLE1)
         + box("warn", "가격 칸은 일부러 비워 두었습니다", "스킬이 가격을 지어내지 않고 [확인 필요]로 두는지 시험하는 장치입니다."),
         ok="설명서에 정한 콘텐츠가 정한 순서대로 나오고, 가격 자리에는 숫자 대신 [확인 필요]가 보이면 성공입니다.",
         stuck=f"AI가 \"가격을 알려 주세요\"처럼 먼저 물어보면 <b>정상</b>입니다(빠진 정보를 묻도록 설명서에 적었기 때문). 아래 문장을 보내세요.{prompt(P_NO_PRICE)}",
         figure=fig("m3-02", "상품 정보를 보내면 콘텐츠가 한 번에 나옴(예시)", ai_window(
             [("user", "[상품 정보] ※ 실습용 가상 상품입니다\n- 상품명: 귤빛담은 수제 감귤잼 …"),
              ("ai", "[1] 인스타그램 게시글\n아이 간식, 성분표부터 보게 되시죠? …\n\n[2] 네이버 블로그 글\n제목: …\n\n[3] 카카오톡 채널 메시지\n…\n\n※ 가격: [확인 필요]")],
             marks={"input": 2}, hist=("스킬 실행 – 감귤잼", "마케팅 스킬 만들기"), hist_on="스킬 실행 – 감귤잼"))),
    step("3-3", "출력물 저장하기", "심사 보조자료로 낼 '샘플 출력물'을 파일로 저장합니다.",
         [f"AI 답변 아래 {ui('⧉ 복사')}를 누릅니다",
          f"메모장에서 {kbd('Ctrl', 'N')}(새 탭)을 누르고 {kbd('Ctrl', 'V')}로 붙여넣습니다",
          f"{ui('파일')} → {ui('다른 이름으로 저장')} → 파일 이름 <b>트랙B_출력물_감귤잼_내이름.txt</b> → {ui('저장')}"],
         ok="메모장 위쪽에 탭이 두 개(스킬, 출력물) 보이면 성공입니다.",
         figure=fig("m3-03", "메모장 새 탭에 출력물 붙여넣기", notepad(
             "[1] 인스타그램 게시글\n아이 간식, 성분표부터 보게 되시죠? …\n\n[2] 네이버 블로그 글\n…", title="트랙B_출력물_감귤잼_내이름.txt",
             tabs=["트랙B_스킬_내이름.txt", "트랙B_출력물_감귤잼_내이름.txt"], text_mark=2))),
]), pc_note=PC)

# ───────────────────────── 4 점검 ─────────────────────────
p4 = wrap("".join([
    tab_hero("🔍", "STEP 4 · 약 20분", "점검하고 고치기", "지어낸 내용이 없는지, 다른 상품에도 되는지 확인합니다"),
    flow([("결과 점검", "지어낸 말 찾기"), ("다른 상품 시험", "필수 ③ 확인"), ("스킬 고치기", "고친 설명서로 바꿔 저장")]),
    step("4-1", "결과물 점검 시키기", "AI에게 방금 결과가 규칙을 지켰는지 스스로 점검하게 합니다.",
         [f"3-2를 한 <b>같은 채팅</b>에서 아래 상자의 {ui('복사')}를 누릅니다",
          f"입력창에 {kbd('Ctrl', 'V')} 후 보내기"],
         extra=prompt(P_CHECK),
         ok="1번(지어낸 내용)과 3번(형식 어긴 곳)이 모두 \"없음\"이면 통과입니다. 문제가 있었다면 4번에 고친 결과가 나오니, 그것으로 출력물 파일을 바꿔 저장하세요.",
         stuck="1번에 문제가 나왔다면 출력물만 고치지 말고, 4-3에서 <b>스킬 설명서도</b> 고쳐야 다음에도 같은 실수를 하지 않습니다.", one=True),
    step("4-2", "다른 상품으로 재사용 시험", "필수 요구사항 ③(다른 상품에도 다시 쓸 수 있음)을 확인합니다.",
         [f"{ui('＋ 새 채팅')}을 누르고 3-1과 똑같이 시작 문장 + 스킬 설명서를 보냅니다",
          f"아래 두 번째 샘플 상품을 {ui('복사')} → 붙여넣기 → 보내기"],
         extra=prompt(SAMPLE2),
         ok="감귤잼 때와 <b>같은 구성·같은 순서</b>로, 노트북 거치대에 맞는 내용이 나오면 성공입니다.",
         stuck="결과에 '감귤', '아이 간식'처럼 첫 번째 상품 이야기가 섞이면 설명서 안에 특정 상품이 들어가 있다는 뜻입니다. 4-3에서 \"특정 상품 이야기를 모두 빼 줘\"로 고치세요.",
         figure=fig("m4-01", "새 채팅에서 두 번째 상품으로 실행", ai_window(
             [("user", "지금부터 붙여넣는 글은 '스킬 설명서'야. …"), ("ai", "상품 정보를 보내 주세요"),
              ("user", "[상품 정보] ※ 실습용 가상 상품입니다\n- 상품명: 폴딩업 노트북 거치대 …")],
             new_mark=1, marks={"send": 2}, hist=("스킬 실행 – 거치대", "스킬 실행 – 감귤잼", "마케팅 스킬 만들기"), hist_on="스킬 실행 – 거치대"))),
    step("4-3", "스킬 설명서 고치기", "시험에서 나온 문제를 설명서에 반영해 더 좋은 스킬로 만듭니다.",
         [f"왼쪽 최근 대화에서 스킬을 만들었던 대화({ui('마케팅 스킬 만들기')} 등)를 누릅니다",
          f"아래 상자를 {ui('복사')} → 입력창에 붙여넣고, <b>[문제]</b> 아래 줄을 내가 겪은 문제로 바꿉니다",
          "보내기를 누릅니다",
          f"새로 나온 설명서를 {ui('⧉ 복사')} → 메모장의 스킬 탭에서 {kbd('Ctrl', 'A')} → {kbd('Ctrl', 'V')} → {kbd('Ctrl', 'S')}(저장)"],
         extra=prompt(P_FIX)
         + table(["이런 문제가 있었다면", "[문제] 칸에 이렇게 쓰세요"], [
             ["글이 너무 길다", "블로그 글은 800자 안쪽으로 줄이는 규칙을 넣어 줘"],
             ["해시태그가 너무 많다", "해시태그는 5개로 정해 줘"],
             ["가격·수치를 지어냈다", "입력에 없는 숫자는 쓰지 말고 [확인 필요]로 쓰라는 규칙을 더 분명하게 넣어 줘"],
             ["다른 상품 이야기가 섞였다", "설명서 안의 특정 상품 이야기를 모두 빼 줘"],
             ["말투가 대상과 안 맞다", "홍보 대상의 나이와 상황에 맞게 말투를 바꾸는 절차를 넣어 줘"]]),
         ok="고친 설명서로 3-1~3-2를 새 채팅에서 다시 돌렸을 때 문제가 사라지면 성공입니다. 출력물 파일도 새 결과로 바꿔 저장하세요.",
         figure=fig("m4-02", "스킬 만든 대화로 돌아가 고치기 요청", ai_window(
             [("ai", skill_preview())], hist=("스킬 실행 – 거치대", "스킬 실행 – 감귤잼", "마케팅 스킬 만들기"), hist_on="마케팅 스킬 만들기",
             hist_mark=1, input_text="스킬 설명서를 시험해 봤더니 아래 문제가 있었어. …", marks={"input": 2, "send": 3}))),
]), pc_note=PC)

# ───────────────────────── 5 제출 ─────────────────────────
p5 = wrap("".join([
    tab_hero("📦", "STEP 5 · 약 10분", "제출 준비", "점검표로 확인하고 파일 2개를 정리합니다"),
    step("5-1", "과제 조건 최종 점검", "내 스킬이 과제 조건을 모두 채웠는지 AI와 함께 확인합니다.",
         [f"{ui('＋ 새 채팅')}을 누르고 아래 상자를 {ui('복사')} → 붙여넣기",
          f"이어서 메모장의 스킬 설명서 전체를 {kbd('Ctrl', 'A')} → {kbd('Ctrl', 'C')} → 입력창 끝에 {kbd('Ctrl', 'V')} → 보내기",
          "'부족'이 나온 조건은 알려 준 문장을 메모장 설명서의 알맞은 번호 아래에 붙여넣고 저장합니다"],
         extra=prompt(P_FINAL),
         ok="다섯 조건이 모두 '충족'이면 끝입니다.", one=True),
    step("5-2", "점검표 확인하고 파일 정리", "제출할 파일 2개를 확인합니다.",
         ["아래 점검표를 하나씩 확인합니다",
          "제출 파일 2개가 있는지 확인합니다",
          "제출 방법(제출 장소·링크)은 현장 운영진 안내를 따릅니다"],
         extra=table(["구분", "확인할 것"], [list(c) for c in CHECKLIST])
         + table(["제출 파일", "이름 예시", "내용"], [
             ["① 스킬", "트랙B_스킬_내이름.txt", "스킬 설명서(0~5번)"],
             ["② 샘플 출력물", "트랙B_출력물_감귤잼_내이름.txt", "샘플 상품으로 실행한 결과(거치대 결과를 함께 붙여도 좋습니다)"]])
         + box("no", "제출 전에 한 번 더", "실제 고객 정보·회사 내부 자료가 들어 있지 않은지, 만든 콘텐츠를 실제로 게시하지 않았는지 확인하세요."),
         ok="파일 2개가 준비되고 점검표가 모두 체크되면 제출 준비 완료입니다. 수고하셨습니다! 🎉", one=True),
]))

# ───────────────────────── 부록 ─────────────────────────
ap = wrap("".join([
    tab_hero("🛟", "APPENDIX", "부록", "막힐 때 찾아보세요"),
    "<h3>자주 막히는 문제</h3>",
    table(["이런 일이 생기면", "원인", "해결"], [
        ["답이 중간에 끊겼다", "답이 길어서 한 번에 다 못 씀", "\"계속\"이라고 보내기"],
        ["답에 표·** 기호가 섞였다", "AI의 기본 꾸밈 습관", "\"메모장용 일반 글자로 다시 써 줘\""],
        ["영어로 답한다", "앞 대화 영향", "\"한국어로 다시 써 줘\" 또는 새 채팅"],
        ["가격·수치를 지어냈다", "규칙이 약함", "4-3에서 '지어내지 않기' 규칙 강화"],
        ["메모장 글자가 깨진다(ㅁㅁ, ??)", "저장 인코딩 문제", "다른 이름으로 저장 → 인코딩 UTF-8"],
        ["\"사용량 한도에 도달\" 안내", "무료 계정의 사용량 제한", "다른 AI(ChatGPT·Claude·Gemini)로 이어서 진행 — 설명서 txt만 있으면 어디서든 됩니다"],
        ["Enter를 눌렀더니 중간에 보내졌다", "Enter = 보내기", f"줄 바꿈은 {kbd('Shift', 'Enter')}"],
    ], raw=True),
    "<h3>AI에게 줘도 되는 것 / 안 되는 것</h3>",
    box("ok", "✅ 줘도 되는 것", "가상 상품 정보, 공개된 상품 소개, 내가 만든 스킬 설명서"),
    box("no", "⛔ 주면 안 되는 것", "고객 이름·전화번호·주소, 회사 내부 문서·매출 자료, 비밀번호·계정 정보"),
    box("info", "💡 요령", "AI 답이 마음에 안 들면 처음부터 다시 쓰지 말고 \"○○ 부분만 바꿔 줘\"처럼 고칠 곳만 말하세요."),
    "<h3>용어 풀이</h3>",
    table(["용어", "뜻"], [["프롬프트", "AI에게 보내는 요청 글"], ["스킬(스킬 설명서)", "상품이 바뀌어도 다시 쓸 수 있게 정리한 AI용 업무 설명서"],
                         ["출력 형식", "결과물의 모양(분량, 순서, 해시태그 수 등)"], ["[확인 필요]", "정보가 없어 사람이 채워야 하는 자리 표시"],
                         ["txt 파일", "글자만 담긴 가장 단순한 문서 파일(메모장으로 만듦)"]]),
    "<h3>되돌리기</h3>",
    f"<p>메모장에서 실수로 지웠다면 {kbd('Ctrl', 'Z')}. 스킬 설명서를 망쳤다면 AI 대화에 남아 있는 이전 답을 다시 복사하면 됩니다.</p>",
    shot_list_section(),
]))

# ───────────────────────── 실습 파일 생성(교안과 같은 원문) ─────────────────────────
blocks = [("1-1 한 줄 부탁(맛보기)", P_TASTE_1), ("1-2 정보와 형식을 주고 부탁(맛보기)", P_TASTE_2),
          ("2-2 스킬 만드는 프롬프트", P_MAKE), ("3-1 새 채팅 시작 문장(이어서 스킬 설명서 붙여넣기)", P_RUN),
          ("3-2 막히면: 가격 없음 안내", P_NO_PRICE), ("3-2 샘플 상품 1", SAMPLE1), ("4-1 결과물 점검", P_CHECK),
          ("4-2 샘플 상품 2", SAMPLE2), ("4-3 스킬 고치기", P_FIX), ("5-1 과제 조건 최종 점검(이어서 스킬 설명서 붙여넣기)", P_FINAL)]
(PRACTICE / "prompts_all.txt").write_text(
    "스마트워크톤 트랙B · 스킬 제작 가이드 — 프롬프트 모음\n" + SITE_URL + "\n\n"
    + "\n\n".join(f"==================== {t} ====================\n{b.strip()}" for t, b in blocks) + "\n", encoding="utf-8")
(PRACTICE / "checklist.txt").write_text(
    "스마트워크톤 트랙B · 제출 전 점검표\n\n" + "\n".join(f"[ ] {a} — {b}" for a, b in CHECKLIST)
    + "\n\n제출 파일\n[ ] ① 트랙B_스킬_내이름.txt\n[ ] ② 트랙B_출력물_감귤잼_내이름.txt\n", encoding="utf-8")

STEP_PAGES = [
    Page("home", "", "홈", home), Page("p0", "0", "준비", p0), Page("p1", "1", "맛보기", p1), Page("p2", "2", "스킬 만들기", p2),
    Page("p3", "3", "실행", p3), Page("p4", "4", "점검·고치기", p4), Page("p5", "5", "제출", p5), Page("ap", "+", "부록", ap)]
add_pager(STEP_PAGES)
STEP_PAGES[0].html = home + ('<nav class="pager" aria-label="시작"><a class="prev" href="#p0" data-go="p0"><small>공통 단계로 →</small><b>0 준비부터 차례로</b></a>'
                             '<a class="next" href="#gpt" data-go="gpt"><small>내 AI 화면으로 →</small><b>🟢 ChatGPT · 🟠 Claude · 🔵 Gemini</b></a></nav>')
MODEL_PAGES = [Page(k, S["icon"], S["name"], model_page(k) + model_pager(k)) for k, S in MODELS.items()]
PAGES = STEP_PAGES[:1] + MODEL_PAGES + STEP_PAGES[1:]

build(DOCS / "index.html", PAGES,
    title="스킬 제작 가이드 | 스마트워크톤 트랙B",
    description="복사·붙여넣기만으로 상품 정보 하나로 마케팅 콘텐츠를 한 번에 만드는 AI 스킬(txt)을 완성하는 단계별 가이드",
    brand=("B", "스킬 제작 가이드", "제5회 스마트워크톤 · 트랙B"),
    site_url=SITE_URL, og_image="og_image.jpg", og_title="스킬 제작 가이드 — 스마트워크톤 트랙B", extra_css=EXTRA_CSS + MODEL_CSS + THEME_CSS)
print("wrote", DOCS / "index.html")
