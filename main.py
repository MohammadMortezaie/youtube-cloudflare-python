from js import Response


async def on_fetch(request, env, ctx):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="theme-color" content="#101412">
        <meta name="description" content="WebPulse builds custom software and AI automations that help ambitious businesses move forward.">
        <title>WebPulse | Software for what's next</title>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
        <style>
            :root {
                color-scheme: light;
                --ink: #101412;
                --paper: #f5f5ef;
                --lime: #d9ff67;
                --muted: #a4aaa2;
                --line: rgba(255, 255, 255, .16);
                --display: 'Space Grotesk', sans-serif;
                --body: 'DM Sans', sans-serif;
            }
            * { box-sizing: border-box; }
            html { scroll-behavior: smooth; }
            body { margin: 0; font-family: var(--body); color: var(--ink); background: var(--paper); }
            a { color: inherit; }
            a:focus-visible { outline: 3px solid #80a900; outline-offset: 4px; }
            .hero-shell { color: var(--paper); background: var(--ink); overflow: hidden; position: relative; }
            .hero-shell::before { content: ''; position: absolute; inset: 0; pointer-events: none; opacity: .14; background-image: radial-gradient(#9ca89a 0.6px, transparent 0.6px); background-size: 18px 18px; mask-image: linear-gradient(100deg, black, transparent 70%); }
            .nav, .hero, .section-inner, .footer-inner { width: min(1180px, calc(100% - 64px)); margin-inline: auto; position: relative; }
            .nav { height: 86px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid var(--line); }
            .brand { display: inline-flex; gap: 11px; align-items: center; text-decoration: none; font: 700 21px var(--display); letter-spacing: 0; }
            .brand-mark { width: 29px; height: 29px; display: grid; place-items: center; background: var(--lime); color: var(--ink); border-radius: 8px; font: 700 17px var(--display); }
            .nav-links { display: flex; align-items: center; gap: 34px; font-size: 13px; color: #c5cbc3; }
            .nav-links a { text-decoration: none; transition: color .2s ease; }
            .nav-links a:hover { color: var(--lime); }
            .nav-cta { display: inline-flex; align-items: center; gap: 12px; padding: 12px 16px; background: var(--lime); color: var(--ink) !important; border-radius: 5px; font-weight: 700; }
            .hero { min-height: 650px; padding-block: 76px 92px; display: grid; grid-template-columns: 1.02fr .98fr; gap: 52px; align-items: center; }
            .eyebrow { display: flex; align-items: center; gap: 10px; color: var(--lime); text-transform: uppercase; font-weight: 700; font-size: 10px; letter-spacing: 1.5px; }
            .eyebrow::before { content: ''; width: 24px; height: 1px; background: currentColor; }
            h1, h2, h3, p { margin-top: 0; }
            h1 { max-width: 610px; margin-block: 24px 22px; font: 600 clamp(48px, 6vw, 76px)/.99 var(--display); letter-spacing: 0; }
            h1 span { color: var(--lime); }
            .hero-copy { max-width: 470px; margin-bottom: 30px; color: #b5bdb4; font-size: 16px; line-height: 1.75; }
            .actions { display: flex; align-items: center; gap: 22px; flex-wrap: wrap; }
            .button-primary { min-height: 50px; display: inline-flex; align-items: center; justify-content: center; gap: 18px; padding: 0 19px; color: var(--ink); background: var(--lime); border-radius: 5px; text-decoration: none; font-size: 13px; font-weight: 700; transition: transform .2s ease, background .2s ease; }
            .button-primary:hover { transform: translateY(-2px); background: #e6ff9b; }
            .text-link { color: #d5dbd3; font-size: 13px; text-decoration-color: #707970; text-underline-offset: 5px; }
            .hero-visual { height: 440px; position: relative; isolation: isolate; }
            .hero-photo { position: absolute; inset: 0 0 24px 35px; overflow: hidden; border-radius: 4px; background: #313c34; }
            .hero-photo::after { content: ''; position: absolute; inset: 0; background: linear-gradient(180deg, transparent 45%, rgba(9, 15, 11, .54)); }
            .hero-photo img { display: block; width: 100%; height: 100%; object-fit: cover; object-position: 50% 48%; filter: saturate(.75); }
            .visual-label { position: absolute; z-index: 1; right: 20px; bottom: 44px; color: white; font: 500 12px var(--display); }
            .visual-label span { color: var(--lime); }
            .signal-card { position: absolute; z-index: 2; left: 0; bottom: 0; width: 228px; padding: 17px; color: var(--ink); background: var(--lime); border-radius: 4px; box-shadow: 0 15px 45px rgba(0, 0, 0, .24); animation: settle .7s .15s both; }
            .signal-top { display: flex; justify-content: space-between; align-items: center; font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: .7px; }
            .signal-dot { width: 7px; height: 7px; border-radius: 50%; background: #236b42; box-shadow: 0 0 0 4px rgba(35, 107, 66, .12); }
            .signal-card strong { display: block; margin-top: 20px; font: 600 34px/.95 var(--display); letter-spacing: 0; }
            .signal-card p { margin: 9px 0 0; font-size: 11px; }
            .signal-line { display: flex; align-items: end; gap: 5px; height: 32px; margin-top: 15px; }
            .signal-line i { flex: 1; background: rgba(16, 20, 18, .7); border-radius: 2px 2px 0 0; animation: grow .7s both; transform-origin: bottom; }
            .signal-line i:nth-child(1) { height: 30%; } .signal-line i:nth-child(2) { height: 52%; animation-delay: .08s; } .signal-line i:nth-child(3) { height: 41%; animation-delay: .16s; } .signal-line i:nth-child(4) { height: 73%; animation-delay: .24s; } .signal-line i:nth-child(5) { height: 59%; animation-delay: .32s; } .signal-line i:nth-child(6) { height: 100%; animation-delay: .4s; }
            .trust-strip { border-top: 1px solid var(--line); color: #c6ccc4; }
            .trust-inner { width: min(1180px, calc(100% - 64px)); min-height: 76px; margin: auto; display: flex; justify-content: space-between; align-items: center; gap: 24px; font-size: 12px; }
            .trust-note { display: flex; align-items: center; gap: 10px; color: var(--lime); font-weight: 600; }
            .trust-note span { color: #c6ccc4; font-weight: 400; }
            .trust-item { color: #899188; font: 600 12px var(--display); }
            .services { padding-block: 105px 112px; }
            .section-kicker { margin-bottom: 15px; color: #647d1a; text-transform: uppercase; font-size: 10px; font-weight: 700; letter-spacing: 1.5px; }
            .section-heading { display: flex; justify-content: space-between; align-items: end; gap: 35px; margin-bottom: 42px; }
            h2 { max-width: 590px; margin-bottom: 0; font: 600 clamp(36px, 4.7vw, 55px)/1.04 var(--display); letter-spacing: 0; }
            .section-intro { max-width: 330px; margin-bottom: 3px; color: #626b63; font-size: 14px; line-height: 1.7; }
            .service-grid { display: grid; grid-template-columns: repeat(3, 1fr); border-top: 1px solid #cdd1c8; border-bottom: 1px solid #cdd1c8; }
            .service { min-height: 248px; padding: 28px 27px 25px 0; }
            .service + .service { border-left: 1px solid #cdd1c8; padding-left: 27px; }
            .service-index { display: flex; justify-content: space-between; color: #758074; font: 500 11px var(--display); }
            .service-icon { width: 34px; height: 34px; display: grid; place-items: center; border: 1px solid #bec5b9; border-radius: 50%; color: #45620c; font: 600 15px var(--display); }
            h3 { margin: 35px 0 10px; font: 600 21px var(--display); letter-spacing: 0; }
            .service p { max-width: 290px; margin-bottom: 0; color: #626b63; font-size: 13px; line-height: 1.7; }
            .approach { background: #e8ebe2; padding-block: 82px; }
            .approach-inner { display: grid; grid-template-columns: .78fr 1.22fr; gap: 90px; align-items: start; }
            .approach h2 { font-size: clamp(36px, 4vw, 48px); }
            .approach-copy { max-width: 380px; margin-top: 19px; color: #626b63; font-size: 14px; line-height: 1.75; }
            .steps { border-top: 1px solid #bec5b9; }
            .step { display: grid; grid-template-columns: 45px 1fr; gap: 17px; padding: 20px 0; border-bottom: 1px solid #bec5b9; }
            .step-number { color: #718927; font: 600 12px var(--display); }
            .step h3 { margin: 0 0 5px; font-size: 16px; }
            .step p { margin: 0; color: #626b63; font-size: 12px; line-height: 1.6; }
            .closing { padding-block: 87px; color: var(--paper); background: var(--ink); position: relative; overflow: hidden; }
            .closing::after { content: ''; position: absolute; width: 380px; height: 380px; right: -80px; top: -215px; border: 1px solid rgba(217, 255, 103, .22); border-radius: 50%; box-shadow: 0 0 0 36px rgba(217, 255, 103, .035), 0 0 0 72px rgba(217, 255, 103, .025); }
            .closing-inner { display: flex; align-items: center; justify-content: space-between; gap: 35px; position: relative; z-index: 1; }
            .closing h2 { max-width: 690px; font-size: clamp(36px, 5vw, 59px); }
            .closing h2 span { color: var(--lime); }
            .closing .button-primary { flex: 0 0 auto; }
            footer { color: #c5cbc3; background: var(--ink); }
            .footer-inner { min-height: 76px; display: flex; justify-content: space-between; align-items: center; gap: 20px; border-top: 1px solid var(--line); font-size: 11px; }
            .footer-inner p { margin: 0; color: #899188; }
            .footer-inner a { text-decoration: none; }
            @keyframes settle { from { opacity: 0; transform: translateY(12px); } to { opacity: 1; transform: translateY(0); } }
            @keyframes grow { from { transform: scaleY(.15); } to { transform: scaleY(1); } }
            @media (prefers-reduced-motion: reduce) { *, *::before, *::after { scroll-behavior: auto !important; animation-duration: .01ms !important; animation-iteration-count: 1 !important; transition-duration: .01ms !important; } }
            @media (max-width: 800px) {
                .nav, .hero, .section-inner, .footer-inner { width: min(100% - 40px, 600px); }
                .nav { height: 72px; }
                .nav-links { gap: 18px; }
                .nav-links > a:not(.nav-cta) { display: none; }
                .hero { min-height: auto; padding-block: 66px 62px; grid-template-columns: 1fr; gap: 44px; }
                h1 { max-width: 570px; font-size: clamp(49px, 10vw, 70px); }
                .hero-visual { height: min(440px, 75vw); min-height: 310px; }
                .hero-photo { left: 24px; }
                .trust-inner { width: min(100% - 40px, 600px); min-height: auto; padding-block: 20px; justify-content: flex-start; flex-wrap: wrap; gap: 14px 24px; }
                .trust-note { flex-basis: 100%; }
                .services { padding-block: 76px; }
                .section-heading { align-items: start; flex-direction: column; gap: 17px; margin-bottom: 30px; }
                .service-grid { grid-template-columns: 1fr; }
                .service { min-height: auto; padding: 22px 0 !important; }
                .service + .service { border-left: 0; border-top: 1px solid #cdd1c8; }
                h3 { margin-top: 22px; }
                .approach { padding-block: 65px; }
                .approach-inner { grid-template-columns: 1fr; gap: 32px; }
                .closing-inner { align-items: start; flex-direction: column; }
                .footer-inner { min-height: 68px; }
            }
            @media (max-width: 420px) {
                .nav, .hero, .section-inner, .footer-inner, .trust-inner { width: calc(100% - 32px); }
                .brand { font-size: 19px; }
                .nav-cta { padding: 10px 11px; gap: 7px; font-size: 11px; }
                .hero { padding-top: 52px; }
                .hero-visual { min-height: 280px; }
                .signal-card { width: 190px; padding: 13px; }
                .signal-card strong { font-size: 29px; }
                .trust-inner { gap: 12px 18px; }
                .trust-item { font-size: 10px; }
                .footer-inner { align-items: start; flex-direction: column; justify-content: center; padding-block: 16px; }
            }
        </style>
    </head>
    <body>
        <header class="hero-shell">
            <nav class="nav" aria-label="Main navigation">
                <a class="brand" href="https://webpulse.ca" aria-label="WebPulse home"><span class="brand-mark">W</span> WebPulse</a>
                <div class="nav-links">
                    <a href="#services">What we do</a>
                    <a href="#approach">Our approach</a>
                    <a class="nav-cta" href="https://webpulse.ca">Let's talk <span aria-hidden="true">↗</span></a>
                </div>
            </nav>
            <main class="hero">
                <div class="hero-content">
                    <div class="eyebrow">Custom software · AI automation</div>
                    <h1>Make your next move your <span>best one.</span></h1>
                    <p class="hero-copy">We build thoughtful software and practical AI automations that clear the busywork, connect your tools, and give your business room to grow.</p>
                    <div class="actions">
                        <a class="button-primary" href="https://webpulse.ca">Build something better <span aria-hidden="true">↗</span></a>
                        <a class="text-link" href="#services">Explore what we do</a>
                    </div>
                </div>
                <div class="hero-visual" aria-label="A team collaborating around a laptop">
                    <div class="hero-photo">
                        <img src="https://images.unsplash.com/photo-1521737711867-e3b97375f902?auto=format&fit=crop&w=1200&q=85" alt="A team sharing ideas around a laptop" fetchpriority="high">
                        <div class="visual-label">Good work, <span>in motion.</span></div>
                    </div>
                    <div class="signal-card" aria-label="Less busywork, more momentum">
                        <div class="signal-top"><span>Momentum, amplified</span><span class="signal-dot"></span></div>
                        <strong>More flow.</strong>
                        <p>Less busywork. More room for what matters.</p>
                        <div class="signal-line" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i></div>
                    </div>
                </div>
            </main>
            <div class="trust-strip">
                <div class="trust-inner">
                    <div class="trust-note">Built around your business <span>— not the other way around.</span></div>
                    <div class="trust-item">MADE TO FIT</div>
                    <div class="trust-item">BUILT TO SCALE</div>
                    <div class="trust-item">READY FOR WHAT'S NEXT</div>
                </div>
            </div>
        </header>
        <section class="services" id="services">
            <div class="section-inner">
                <div class="section-kicker">A smarter way forward</div>
                <div class="section-heading">
                    <h2>Technology that works like you do.</h2>
                    <p class="section-intro">The right tools should make work feel lighter. We design and build the pieces that make it happen.</p>
                </div>
                <div class="service-grid">
                    <article class="service">
                        <div class="service-index"><span>01 / BUILD</span><span class="service-icon" aria-hidden="true">↗</span></div>
                        <h3>Custom software</h3>
                        <p>Purpose-built web apps and digital tools designed around your team's real workflow, not a one-size-fits-all template.</p>
                    </article>
                    <article class="service">
                        <div class="service-index"><span>02 / AUTOMATE</span><span class="service-icon" aria-hidden="true">✳</span></div>
                        <h3>AI automation</h3>
                        <p>Let AI handle repeatable tasks, move information where it belongs, and give your people time back.</p>
                    </article>
                    <article class="service">
                        <div class="service-index"><span>03 / CONNECT</span><span class="service-icon" aria-hidden="true">⤳</span></div>
                        <h3>Systems integration</h3>
                        <p>Connect the platforms you already rely on, so your tools share context and your work keeps moving.</p>
                    </article>
                </div>
            </div>
        </section>
        <section class="approach" id="approach">
            <div class="section-inner approach-inner">
                <div>
                    <div class="section-kicker">Small steps. Real momentum.</div>
                    <h2>From tangled workflow to clear next step.</h2>
                    <p class="approach-copy">No off-the-shelf answer forced into your business. We start by understanding where the friction is, then build what actually helps.</p>
                </div>
                <div class="steps">
                    <div class="step"><div class="step-number">01</div><div><h3>Find the friction</h3><p>We get close to how your team works and identify where time and energy are getting lost.</p></div></div>
                    <div class="step"><div class="step-number">02</div><div><h3>Design the right fix</h3><p>Together, we map a practical solution with a clear purpose and a plan to get there.</p></div></div>
                    <div class="step"><div class="step-number">03</div><div><h3>Build, launch, improve</h3><p>We bring it to life, then keep making it better as your business moves forward.</p></div></div>
                </div>
            </div>
        </section>
        <section class="closing">
            <div class="section-inner closing-inner">
                <h2>Your next great idea deserves a <span>better way.</span></h2>
                <a class="button-primary" href="https://webpulse.ca">Start a conversation <span aria-hidden="true">↗</span></a>
            </div>
        </section>
        <footer>
            <div class="footer-inner">
                <a class="brand" href="https://webpulse.ca"><span class="brand-mark">W</span> WebPulse</a>
                <p>Custom software &amp; AI automation</p>
                <a href="https://webpulse.ca">webpulse.ca ↗</a>
            </div>
        </footer>
    </body>
    </html>
    """

    return Response.new(
        html_content,
        headers=[("content-type", "text/html;charset=UTF-8")]
    )
