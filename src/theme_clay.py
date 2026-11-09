"""파스텔 클레이 3D 테마 — google-flow-course 교안의 색감·클레이 질감·떠다니는 모션을 lessonkit 교안에 입힌다.
lesson.css는 그대로 두고 build(extra_css=...)로 덮어쓴다."""
from lessonkit import E

THEME_CSS = r"""
:root{--ink:#1d1f33;--pu:#7c5cff;--pu2:#5b4fe0;--pul:#f0edff;--mk:#ff3d84;--navy:#2a2563;--bd:#ecebf4;--bg:#f4f2fa;
  --acc1:#9b8bff;--acc2:#5b4fe0;--accl:#f0edff;--accl2:#fdf0f6}
body{background:#f7f6fb}
.page{overflow-x:clip}
.nav{background:rgba(255,255,255,.86);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border-bottom:1px solid #eeecf6}
.brand .logo{border-radius:12px;color:#fff;background:radial-gradient(circle at 30% 25%,#fff 0,#c9bcff 30%,#7c66ff 75%);box-shadow:0 6px 14px -6px rgba(124,102,255,.7),inset 0 -3px 6px rgba(60,40,160,.25)}
.tab.on{color:var(--pu2);border-bottom-color:var(--pu)}
.tab.on .tnum{background:var(--pul);color:var(--pu2)}
h2.sec{color:var(--ink)}
.ui{color:var(--pu2);background:var(--pul)}
a{color:var(--pu2)}
/* ── 표지 ── */
.hero.clay{text-align:left;color:var(--ink);padding:42px 24px 54px;background:linear-gradient(135deg,#efeaff 0%,#fde9f2 55%,#fff1e6 100%);position:relative;overflow:hidden}
.hero-in{max-width:1120px;margin:0 auto;display:grid;grid-template-columns:1fr 1.05fr;gap:34px;align-items:center}
.hero.clay .eb{background:#fff;color:#5a4bd6;border:1px solid #fff;box-shadow:0 6px 16px -8px rgba(110,90,200,.45)}
.hero.clay h1{color:var(--ink)}
.hero.clay h1 em{background:linear-gradient(90deg,#7c5cff,#ff6fa5 55%,#ff9a62);-webkit-background-clip:text;background-clip:text;color:transparent}
.hero.clay p{color:#4a4f66;margin:0 0 20px;max-width:none}
.pills{display:flex;gap:8px;flex-wrap:wrap}
.pills span{padding:6px 15px;background:rgba(255,255,255,.8);border:1px solid #fff;color:#3b3e5c;border-radius:999px;font-size:13px;font-weight:700;box-shadow:0 4px 12px -6px rgba(100,90,170,.35)}
/* 클레이 장면 */
.scene{position:relative;height:340px;perspective:1100px}
.stage{position:absolute;inset:0;transform-style:preserve-3d;animation:tilt 9s ease-in-out infinite}
@keyframes tilt{0%,100%{transform:rotateX(10deg) rotateY(-14deg)}50%{transform:rotateX(4deg) rotateY(-4deg)}}
.c-doc{position:absolute;left:12%;top:26px;width:52%;height:270px;border-radius:28px;background:linear-gradient(160deg,#ffffff,#f1eeff);
  box-shadow:0 34px 50px -26px rgba(105,85,175,.55),inset 0 -8px 16px rgba(124,102,255,.14),inset 0 4px 0 #fff;padding:20px;transform:translateZ(30px);animation:floaty 7s ease-in-out infinite}
.c-doc .h{display:flex;align-items:center;gap:10px;font-weight:900;color:var(--ink);font-size:17px;margin-bottom:14px}
.c-doc .h i{width:34px;height:34px;border-radius:11px;background:radial-gradient(circle at 30% 25%,#fff 0,#c9bcff 30%,#7c66ff 80%);box-shadow:0 6px 12px -5px rgba(106,85,232,.7)}
.c-doc .ln{height:12px;border-radius:999px;margin:11px 0;background:linear-gradient(90deg,#e4defe,#f3e8fb);box-shadow:inset 0 2px 3px rgba(90,70,180,.12)}
.c-doc .ln.s{width:62%}.c-doc .ln.m{width:80%}
.c-doc .tag{display:inline-block;margin:8px 6px 0 0;padding:4px 11px;border-radius:999px;font-size:12px;font-weight:800;color:#fff;background:linear-gradient(135deg,#ff9ac2,#ff5c98);box-shadow:0 6px 12px -6px rgba(255,80,150,.8),inset 0 2px 0 rgba(255,255,255,.4)}
.c-doc .tag.b{background:linear-gradient(135deg,#7fe0c9,#1f9a86);box-shadow:0 6px 12px -6px rgba(31,154,134,.8),inset 0 2px 0 rgba(255,255,255,.4)}
.c-out{position:absolute;right:2%;width:38%;padding:12px 14px;border-radius:20px;font-weight:800;font-size:14px;color:var(--ink);display:flex;align-items:center;gap:9px;
  box-shadow:0 20px 30px -18px rgba(90,80,160,.6),inset 0 -5px 10px rgba(0,0,0,.06),inset 0 3px 0 rgba(255,255,255,.8);animation:floaty 6s ease-in-out infinite}
.c-out{white-space:nowrap}
.c-out b{width:28px;height:28px;border-radius:50%;flex-shrink:0;box-shadow:inset 0 -3px 5px rgba(0,0,0,.15),inset 0 3px 3px rgba(255,255,255,.6)}
.c-out.a{top:18px;background:linear-gradient(145deg,#ffe3ef,#ffc7dc);transform:translateZ(70px)}.c-out.a b{background:radial-gradient(circle at 32% 28%,#fff 0,#ff9ac2 35%,#ff4f93 90%)}
.c-out.b{top:122px;background:linear-gradient(145deg,#e6f9f3,#bfeedf);transform:translateZ(90px);animation-delay:-2s}.c-out.b b{background:radial-gradient(circle at 32% 28%,#fff 0,#a9eadb 35%,#1f9a86 90%)}
.c-out.c{top:226px;background:linear-gradient(145deg,#fff2e6,#ffd9bd);transform:translateZ(60px);animation-delay:-4s}.c-out.c b{background:radial-gradient(circle at 32% 28%,#fff 0,#ffd2b8 35%,#ff8a4a 90%)}
.orb{position:absolute;z-index:2;border-radius:50%;animation:floaty 6s ease-in-out infinite;pointer-events:none}
.o1{width:58px;height:58px;left:0;top:12%;background:radial-gradient(circle at 32% 28%,#fff 0,#d6ccff 28%,#8f7bff 72%,#6a55e8 100%);box-shadow:0 14px 22px -10px rgba(106,85,232,.6);animation-delay:-1s}
.o2{width:52px;height:52px;right:36%;top:-6px;border:12px solid #ffb3d1;box-shadow:0 12px 20px -10px rgba(255,110,170,.6),inset 0 3px 4px rgba(255,255,255,.6);animation-delay:-3s}
.o3{width:30px;height:30px;left:8%;bottom:6px;background:radial-gradient(circle at 32% 28%,#fff 0,#ffd2b8 30%,#ff9a62 80%);box-shadow:0 10px 16px -8px rgba(255,140,90,.6);animation-delay:-2s}
.o4{width:40px;height:40px;right:40%;bottom:-4px;border-radius:12px;background:linear-gradient(145deg,#b6f1e2,#5fd3b8);box-shadow:0 12px 18px -8px rgba(60,170,140,.6),inset 0 3px 3px rgba(255,255,255,.6);animation:floatspin 8s ease-in-out infinite}
@keyframes floaty{0%,100%{translate:0 0}50%{translate:0 -10px}}
@keyframes floatspin{0%,100%{transform:translateY(0) rotate(12deg)}50%{transform:translateY(-12px) rotate(-8deg)}}
/* ── 탭 머리 배너 ── */
.thero{position:relative;display:flex;align-items:center;gap:18px;margin:6px 0 18px;padding:22px 24px;border-radius:26px;border:1px solid #fff;
  background:linear-gradient(135deg,var(--accl),var(--accl2));box-shadow:0 14px 30px -20px rgba(110,90,190,.45);overflow:hidden}
.thero .big{width:66px;height:66px;flex-shrink:0;border-radius:22px;display:flex;align-items:center;justify-content:center;font-size:32px;
  background:linear-gradient(145deg,var(--acc1),var(--acc2));
  box-shadow:0 14px 22px -10px var(--acc2),inset 0 -6px 10px rgba(0,0,0,.14),inset 0 4px 4px rgba(255,255,255,.55);animation:floatspin 8s ease-in-out infinite}
.thero .num{font-size:12px;font-weight:900;letter-spacing:.12em;color:var(--acc2)}
.thero h2{font-size:clamp(21px,3vw,28px);font-weight:900;letter-spacing:-.02em;color:var(--ink);line-height:1.25}
.thero p{font-size:14px;color:#4a4f66;font-weight:600;margin-top:2px}
.thero::after{content:"";position:absolute;right:-26px;top:-26px;width:110px;height:110px;border-radius:50%;
  background:radial-gradient(circle at 32% 28%,rgba(255,255,255,.95) 0,rgba(255,255,255,.4) 40%,transparent 70%)}
/* 탭별 강조색 */
#p0{--acc1:#7fe0c9;--acc2:#178a77;--accl:#e7f8f3;--accl2:#eef1ff}
#p1{--acc1:#ffab7a;--acc2:#e0561f;--accl:#fff1e8;--accl2:#ffeef3}
#p2{--acc1:#9b8bff;--acc2:#5b4fe0;--accl:#f0edff;--accl2:#fdf0f6}
#p3{--acc1:#ff9ac2;--acc2:#e0246d;--accl:#fdeef5;--accl2:#f3efff}
#p4{--acc1:#8fd0ff;--acc2:#2f74d0;--accl:#e9f2ff;--accl2:#eefbf6}
#p5{--acc1:#ffd27a;--acc2:#c98a0b;--accl:#fff7e3;--accl2:#fff0ea}
#ap{--acc1:#c3c7d6;--acc2:#5d6378;--accl:#f2f2f7;--accl2:#ede9fa}
/* ── 단계 카드 ── */
.step{border:1px solid var(--bd);border-radius:24px;box-shadow:0 16px 34px -24px rgba(90,80,160,.5),inset 0 1px 0 #fff;scroll-margin-top:84px}
.step-h{background:linear-gradient(135deg,var(--accl),var(--accl2));color:var(--ink);border-bottom:1px solid #f0eef7}
.step-h .no{color:#fff;border-radius:999px;padding:5px 14px;background:linear-gradient(135deg,var(--acc1),var(--acc2));box-shadow:0 8px 16px -8px var(--acc2),inset 0 2px 0 rgba(255,255,255,.35)}
.page.show .step,.page.show .thero{animation:rise .55s cubic-bezier(.2,.8,.2,1) both}
@keyframes rise{from{opacity:0;transform:perspective(900px) rotateX(10deg) translateY(18px)}to{opacity:1;transform:none}}
ol.do>li::before{background:radial-gradient(circle at 32% 28%,#ffd0e2 0,#ff4f93 45%,#e0246d 100%);box-shadow:0 5px 10px -4px rgba(224,36,109,.7),inset 0 2px 0 rgba(255,255,255,.35)}
.okline,.stuck{border-radius:16px}
.okline{background:linear-gradient(135deg,#e7f8f3,#f0fbf7)}
.stuck{background:linear-gradient(135deg,#fff6e3,#fff1ea)}
.box{border-radius:18px;box-shadow:0 10px 22px -18px rgba(90,80,160,.45)}
.box.info{background:linear-gradient(135deg,#f0edff,#f6f1ff);border-color:#e3dcff}
.box.ok{background:linear-gradient(135deg,#e7f8f3,#effaf6);border-color:#c9eee2}
.box.warn{background:linear-gradient(135deg,#fff6e3,#fff1ea);border-color:#f6e1b4}
.box.no{background:linear-gradient(135deg,#ffeef4,#fff1f0);border-color:#f8cfdc}
.card{border:1px solid var(--bd);border-radius:22px;box-shadow:0 14px 30px -18px rgba(90,80,160,.45),inset 0 1px 0 #fff;transition:transform .2s,box-shadow .2s}
.card:hover{transform:perspective(800px) rotateX(4deg) translateY(-5px);box-shadow:0 22px 36px -20px rgba(90,80,160,.55)}
.card .ic{width:52px;height:52px;border-radius:17px;display:flex;align-items:center;justify-content:center;margin-bottom:10px;
  background:linear-gradient(145deg,#fff,#efeaff);box-shadow:0 10px 18px -10px rgba(106,85,232,.6),inset 0 -4px 6px rgba(124,102,255,.15)}
.card h3{color:var(--ink)}
.flow{gap:10px}
.flow .fs{border:1px solid #fff;border-radius:20px;background:linear-gradient(160deg,#fff,#f4f1ff);box-shadow:0 14px 28px -18px rgba(90,80,160,.45),inset 0 1px 0 #fff;transition:transform .2s}
.flow .fs:hover{transform:translateY(-5px)}
.flow .fs b{color:var(--pu2)}
.flow .ar{color:#c4b8ff}
table.t{border-radius:16px;overflow:hidden}
table.t th{background:#f2effb;color:#4b4672}
.dl{border-radius:16px;background:linear-gradient(135deg,#9b8bff,#5b4fe0);box-shadow:0 10px 18px -10px rgba(91,79,224,.8),inset 0 2px 0 rgba(255,255,255,.3);transition:transform .15s}
.dl.g{background:linear-gradient(135deg,#ff9ac2,#ff5c98);box-shadow:0 10px 18px -10px rgba(255,80,150,.8),inset 0 2px 0 rgba(255,255,255,.3)}
.dl:hover{transform:translateY(-3px)}
.prompt{border:1.5px dashed #c4b8ff;background:linear-gradient(160deg,#fdfcff,#f7f4ff);border-radius:18px;box-shadow:0 10px 22px -18px rgba(90,80,160,.45)}
.prompt .copy-btn{background:linear-gradient(135deg,#9b8bff,#5b4fe0);border-color:transparent;border-radius:999px;box-shadow:0 6px 12px -6px rgba(91,79,224,.8)}
figure.shot{border:1px solid #e6e3f2;border-radius:18px;box-shadow:0 22px 40px -24px rgba(60,50,120,.5)}
.video{border-radius:26px;background:linear-gradient(135deg,#efeaff,#fde9f2 55%,#fff1e6);box-shadow:0 26px 50px -28px rgba(105,85,175,.6),inset 0 1px 0 #fff}
.video .ph{color:var(--ink)}
.video .ph b{color:var(--pu2)}
@media(max-width:860px){.hero-in{grid-template-columns:1fr}.scene{height:300px;max-width:520px;width:100%}.c-doc{left:4%;width:58%;height:240px}}
@media(max-width:520px){.thero{padding:16px;gap:12px;border-radius:22px}.thero .big{width:52px;height:52px;font-size:26px;border-radius:18px}.scene{height:270px}.o2{right:auto;left:38%;top:-14px;width:40px;height:40px;border-width:9px}.c-out{font-size:12.5px;padding:9px 10px}.c-doc .h{font-size:15px}}
@media(prefers-reduced-motion:reduce){.stage,.c-doc,.c-out,.orb,.o4,.thero .big{animation:none!important}.page.show .step,.page.show .thero{animation:none}.card:hover,.flow .fs:hover{transform:none}}
@media print{.stage,.c-doc,.c-out,.orb,.thero .big,.step,.thero{animation:none!important}}
"""


def clay_hero(eyebrow, title_html, desc, pills):
    pill_html = "".join(f"<span>{E(p)}</span>" for p in pills)
    scene = ('<div class="scene" aria-hidden="true"><div class="stage">'
             '<div class="c-doc"><div class="h"><i></i>skill.txt</div><div class="ln"></div><div class="ln m"></div><div class="ln s"></div>'
             '<div class="ln"></div><div class="ln m"></div><span class="tag">상품 특징</span><span class="tag b">홍보 대상</span></div>'
             '<div class="c-out a"><b></b>인스타그램</div><div class="c-out b"><b></b>블로그</div><div class="c-out c"><b></b>카톡 메시지</div>'
             '</div><span class="orb o1"></span><span class="orb o2"></span><span class="orb o3"></span><span class="orb o4"></span></div>')
    return (f'<div class="hero clay"><div class="hero-in"><div><div class="eb">{E(eyebrow)}</div><h1>{title_html}</h1>'
            f'<p>{E(desc)}</p><div class="pills">{pill_html}</div></div>{scene}</div></div>')


def tab_hero(icon, num, title, sub):
    return (f'<div class="thero"><div class="big">{icon}</div><div><div class="num">{E(num)}</div>'
            f'<h2>{E(title)}</h2><p>{E(sub)}</p></div></div>')
