# Rule-based chatbot for TanavDrishti
# Supports detailed responses with keyword matching

RESPONSES = {
    # Greetings
    'hello': "Hi! I'm TanavBot 🤖 I'm your personal mental health assistant. I can help you with stress, anxiety, sleep problems, exam pressure, focus issues and more. What's on your mind today?",
    'hi': "Hey there! 👋 How are you feeling today? You can ask me about stress relief, sleep tips, anxiety, exam pressure, or just type 'helpline' for emergency contacts.",
    'hey': "Hey! 😊 I'm here to support you. What would you like help with today - stress, sleep, studies, or something else?",
    'good morning': "Good morning! 🌅 Starting the day right matters a lot for mental health. Have you slept well? Eaten breakfast? Small habits make a big difference.",
    'good night': "Good night! 🌙 Try to sleep by 11 PM. Avoid your phone 30 minutes before bed. A good night's sleep reduces stress by 40%. Rest well!",

    # Stress
    'stress': (
        "Stress is very common among students, but it can be managed! Here's what helps:\n\n"
        "1. **Breathe** - Try box breathing: inhale 4 sec, hold 4 sec, exhale 4 sec, hold 4 sec. Repeat 4 times.\n"
        "2. **Break tasks** - Don't look at everything at once. Write down 3 tasks for today only.\n"
        "3. **Move your body** - Even a 10-minute walk outside reduces cortisol (stress hormone) significantly.\n"
        "4. **Talk to someone** - Don't bottle it up. A friend, family member, or counselor can help.\n"
        "5. **Limit news and social media** - Constant scrolling increases anxiety and stress.\n\n"
        "Would you like more tips on a specific area - sleep, studies, or social pressure?"
    ),
    'stressed': (
        "I hear you. Feeling stressed is tough, especially during college. Let's tackle it:\n\n"
        "Right now: Splash cold water on your face, take 5 deep breaths, and drink a glass of water.\n\n"
        "Today: Write down what's stressing you - getting it out of your head onto paper reduces its power.\n\n"
        "This week: Identify ONE thing causing the most stress and make a small plan to address it.\n\n"
        "You're not alone in this. What's stressing you most right now - studies, relationships, or something else?"
    ),
    'tension': (
        "Tension usually builds when we feel out of control. Try this:\n\n"
        "- Write down everything worrying you right now\n"
        "- Circle what you CAN control\n"
        "- For things you can't control - accept them and focus energy elsewhere\n\n"
        "Also, progressive muscle relaxation helps: tense and release each muscle group from feet to head. Try it lying down for 10 minutes."
    ),

    # Anxiety
    'anxiety': (
        "Anxiety is your brain's alarm system going off too often. Here's how to calm it:\n\n"
        "**Immediate relief (5-4-3-2-1 technique):**\n"
        "- 5 things you can SEE\n"
        "- 4 things you can TOUCH\n"
        "- 3 things you can HEAR\n"
        "- 2 things you can SMELL\n"
        "- 1 thing you can TASTE\n\n"
        "This grounds you in the present and stops anxious thoughts.\n\n"
        "**Long term:** Regular exercise, limiting caffeine, and consistent sleep schedule significantly reduce anxiety. "
        "If anxiety is affecting your daily life, please talk to a counselor. Tele-MANAS: 14416 (free)."
    ),
    'anxious': (
        "It's okay to feel anxious. Take a moment right now:\n\n"
        "Breathe in slowly for 4 counts... hold for 2... breathe out for 6 counts. Do this 5 times.\n\n"
        "Anxiety often comes from overthinking future events. Ask yourself: 'What is actually happening RIGHT NOW?' "
        "Usually, the present moment is manageable.\n\n"
        "If anxiety is frequent, consider talking to your college counselor - it's completely confidential and free."
    ),
    'panic': (
        "If you're having a panic attack right now:\n\n"
        "1. SIT DOWN and remind yourself: 'This will pass. I am safe.'\n"
        "2. Focus on ONE object in the room. Describe it in detail in your mind.\n"
        "3. Breathe slowly - in for 4 counts, out for 6. Don't breathe too fast.\n"
        "4. Feel your feet on the floor. Press them down firmly.\n\n"
        "Panic attacks typically last 10-20 minutes and then pass. You are not in danger.\n\n"
        "After it passes, drink water and rest. If panic attacks are frequent, please contact:\n"
        "Tele-MANAS: 14416 | iCall: 9152987821"
    ),
    'panic attack': (
        "Stay calm - I'm here. Do this right now:\n\n"
        "Step 1: Sit or lie down somewhere safe.\n"
        "Step 2: Say out loud - 'I am having a panic attack. It will pass. I am not dying.'\n"
        "Step 3: Put one hand on your chest, one on your belly. Breathe so only your belly moves.\n"
        "Step 4: Count slowly to 10, then back to 1.\n\n"
        "You will be okay. Please call Tele-MANAS 14416 if this happens frequently."
    ),

    # Depression
    'depression': (
        "I'm really glad you reached out. Depression is a real medical condition, not a weakness.\n\n"
        "Signs to watch for: feeling sad most of the day, loss of interest in things you used to enjoy, "
        "changes in sleep or appetite, feeling worthless, difficulty concentrating.\n\n"
        "Please don't fight this alone:\n"
        "- Talk to someone you trust today\n"
        "- Contact your college counselor\n"
        "- Call Tele-MANAS: 14416 (free, 24x7, confidential)\n"
        "- iCall: 9152987821\n\n"
        "Small steps help: go outside for 10 minutes, eat one proper meal, call one friend. "
        "You deserve support and care."
    ),
    'depressed': (
        "Thank you for sharing this with me. Feeling depressed is hard, and it takes courage to acknowledge it.\n\n"
        "Right now, please do one small thing: text or call one person you trust and just say 'I'm not doing well.'\n\n"
        "Professional help is available and effective. Your college may have a free counseling center.\n\n"
        "Emergency support:\n"
        "- Tele-MANAS: 14416 (Govt. of India, free, 24x7)\n"
        "- iCall: 9152987821\n"
        "- Vandrevala Foundation: 1860-2662-345\n\n"
        "You are not alone. Things can and do get better with the right support."
    ),
    'sad': (
        "It's completely okay to feel sad sometimes. Emotions are valid.\n\n"
        "A few things that help:\n"
        "- Write in a journal - even 5 minutes of writing releases emotional tension\n"
        "- Listen to music that matches your mood first, then gradually switch to uplifting songs\n"
        "- Go outside, even briefly - sunlight increases serotonin naturally\n"
        "- Do one small kind thing for yourself today\n\n"
        "If sadness stays for more than 2 weeks and affects your daily life, please talk to a counselor."
    ),

    # Sleep
    'sleep': (
        "Sleep is the foundation of mental health. Poor sleep increases stress, anxiety and poor concentration by 60%.\n\n"
        "**Tonight:**\n"
        "- Put phone away 30 min before bed (blue light delays sleep)\n"
        "- Keep room cool and dark\n"
        "- Try reading or light stretching instead of scrolling\n\n"
        "**This week:**\n"
        "- Fix a sleep and wake time - even on weekends\n"
        "- Avoid caffeine after 4 PM\n"
        "- Don't study in bed - your brain should associate bed only with sleep\n\n"
        "Ideal sleep for students: 7 to 9 hours. How many hours are you currently getting?"
    ),
    'cant sleep': (
        "Not being able to sleep is frustrating. Try this tonight:\n\n"
        "1. Get out of bed if you've been lying awake for 20+ minutes. Sit somewhere dim and read.\n"
        "2. Try the military sleep method: relax your face, drop your shoulders, breathe out, relax your legs, and clear your mind for 10 seconds.\n"
        "3. Write down tomorrow's worries before bed - it clears your mind.\n"
        "4. 4-7-8 breathing: inhale 4 sec, hold 7 sec, exhale 8 sec.\n\n"
        "Consistent sleep timing (same time every day) is the single most powerful fix for sleep problems."
    ),
    'insomnia': (
        "Insomnia affects many students. Here's a proper plan:\n\n"
        "**Short term:** Melatonin (0.5mg, consult a doctor), chamomile tea, or warm milk before bed.\n\n"
        "**Behavioral fixes:**\n"
        "- Go to bed only when sleepy, not at a set time\n"
        "- Use bed ONLY for sleep - no studying, no phone\n"
        "- Keep bedroom cool (18-20°C is ideal)\n"
        "- No screens 1 hour before bed\n\n"
        "If insomnia persists for more than 3 weeks, please see a doctor. It's treatable."
    ),

    # Study & Focus
    'study': (
        "Effective studying is about quality, not hours. Here's what works:\n\n"
        "**Pomodoro Technique:**\n"
        "- Study focused for 25 minutes\n"
        "- Take a 5-minute break\n"
        "- After 4 cycles, take a 20-30 minute break\n\n"
        "**Better retention:**\n"
        "- Active recall: close your notes and try to remember what you just read\n"
        "- Spaced repetition: review topics after 1 day, 3 days, 1 week\n"
        "- Teach it: explain concepts aloud as if teaching someone\n\n"
        "**Environment:** Phone in another room, one tab open, water bottle nearby. What subject are you struggling with?"
    ),
    'focus': (
        "Struggling to focus is very common - here's why and how to fix it:\n\n"
        "**Why it happens:** Too many tabs open mentally (worries, notifications, fatigue)\n\n"
        "**Immediate fix:**\n"
        "- Write down all distracting thoughts on paper - now your brain can let them go\n"
        "- Put phone in another room (not just face down - out of sight)\n"
        "- Set a 10-minute timer and just START. Getting started is the hardest part.\n\n"
        "**Tools:** Forest app (blocks phone), Focusmate (virtual study buddy), lo-fi music without lyrics\n\n"
        "**Physical:** Drink water, eat something, ensure you slept enough. Brain fog is often dehydration."
    ),
    'concentrate': (
        "Can't concentrate? Let's fix it:\n\n"
        "First check: Are you hungry? Tired? Dehydrated? Fix those first.\n\n"
        "Then: Clear your desk completely except what you need RIGHT NOW.\n\n"
        "Try the 2-minute rule: tell yourself you'll study for just 2 minutes. Almost always, you'll continue.\n\n"
        "If your mind wanders, gently bring it back without judging yourself. Concentration is a skill - it improves with practice."
    ),
    'exam': (
        "Exam stress is real and valid. Here's a complete plan:\n\n"
        "**1-2 weeks before:**\n"
        "- Make a topic list, prioritize high-weightage areas\n"
        "- Study in blocks, not marathon sessions\n"
        "- Practice past papers - most important step\n\n"
        "**Night before:**\n"
        "- Stop studying by 9-10 PM\n"
        "- Prepare your bag, ID, pen the night before\n"
        "- Sleep at least 7 hours - memory consolidates during sleep\n\n"
        "**Morning of exam:**\n"
        "- Eat a proper breakfast\n"
        "- Arrive early\n"
        "- If you blank: breathe, skip the question, come back\n\n"
        "Remember: one exam does not define your worth or future."
    ),
    'study tips': (
        "Top evidence-based study tips:\n\n"
        "1. **Active recall** beats re-reading every time. Test yourself constantly.\n"
        "2. **Spaced repetition** - use Anki app to review at perfect intervals.\n"
        "3. **Interleaving** - mix different subjects/topics, don't do all of one then all of another.\n"
        "4. **Sleep between sessions** - a nap after studying improves memory retention by 20%.\n"
        "5. **Handwrite notes** - proven to improve understanding vs typing.\n"
        "6. **Teach someone** - if you can explain it simply, you understand it deeply."
    ),

    # Loneliness & Social
    'lonely': (
        "Feeling lonely in college is more common than you think - and it's painful.\n\n"
        "Small steps that help:\n"
        "- Say hi to one classmate tomorrow - just one\n"
        "- Join one club, society, or online community around something you already like\n"
        "- Call a family member or old friend - even a 10-minute call helps\n"
        "- Attend one college event, even just to observe\n\n"
        "Loneliness often comes from waiting for others to reach out first. Taking the first small step, "
        "even if awkward, usually works. You deserve connection."
    ),
    'alone': (
        "Being alone and feeling lonely are different things - but if you're struggling, here's help:\n\n"
        "You can build connection by:\n"
        "- Showing up consistently to the same place (class, library, gym) - familiarity builds friendships naturally\n"
        "- Asking one person a genuine question about themselves\n"
        "- Volunteering - shared purpose creates instant community\n\n"
        "Also: comfortable solitude is a strength. Learning to enjoy your own company is valuable. "
        "But if loneliness is affecting your mental health, please talk to a counselor."
    ),

    # Physical health
    'tired': (
        "Constant tiredness in students is usually caused by poor sleep, poor diet, or burnout.\n\n"
        "Check:\n"
        "- Sleep: Are you getting 7-9 hours? Even one hour less affects performance significantly.\n"
        "- Diet: Skipping meals causes energy crashes. Eat breakfast even if small.\n"
        "- Iron deficiency: Very common in students, causes fatigue. Consider getting a blood test.\n"
        "- Screen time: 6+ hours of screens daily causes mental fatigue.\n\n"
        "Quick energy boost: 20-minute power nap + 1 glass of water + 5 minutes of sunlight."
    ),
    'headache': (
        "Student headaches are usually from:\n"
        "- Dehydration (most common) - drink 2 glasses of water right now\n"
        "- Eye strain from screens - take a 20-20-20 break: every 20 min, look 20 feet away for 20 seconds\n"
        "- Tension from stress - gentle neck stretches help\n"
        "- Poor posture while studying\n\n"
        "If headaches are frequent and severe, please see a doctor."
    ),

    # Motivation
    'motivation': (
        "Lost motivation? Here's the truth: motivation follows action, not the other way around.\n\n"
        "Don't wait to feel motivated - start tiny:\n"
        "- Open the book to the right page. That's it. Often you'll continue.\n"
        "- Commit to 2 minutes, not 2 hours\n"
        "- Remove friction: have your study materials ready before you sit down\n\n"
        "Also identify WHY you're studying - your goal, your reason. Write it on a sticky note and stick it to your desk.\n\n"
        "External tip: Study with someone else. Social accountability is powerful."
    ),
    'give up': (
        "Please don't give up. I know things feel overwhelming right now, but this feeling is temporary.\n\n"
        "Can you tell me more about what's making you want to give up? Is it a subject, a situation, or everything at once?\n\n"
        "What you're feeling is valid. Many successful people felt exactly this way at some point. "
        "One step at a time is enough.\n\n"
        "If you're having thoughts of harming yourself, please call immediately:\n"
        "Tele-MANAS: 14416 (free, 24x7)"
    ),

    # Helpline
    'helpline': (
        "Emergency Mental Health Helplines (India) 🆘\n\n"
        "- Tele-MANAS (Govt. of India): 14416 - FREE, 24x7, Hindi & English\n"
        "- iCall (TISS Mumbai): 9152987821 - Mon-Sat, 8am-10pm\n"
        "- Vandrevala Foundation: 1860-2662-345 - 24x7\n"
        "- AASRA: 9820466627 - 24x7\n"
        "- iCall Email: icall@tiss.edu\n\n"
        "All calls are confidential. Please reach out - you don't have to go through this alone."
    ),

    # Maintain health
    'maintain mental health': (
        "Great that you want to maintain your mental well-being! Here's a daily routine:\n\n"
        "Morning: 5 min sunlight + glass of water + no phone for first 30 min\n"
        "Day: Pomodoro for studies, short walks between sessions\n"
        "Evening: Physical activity (even 20 min walk), connect with someone\n"
        "Night: No screens 30 min before bed, journal 3 good things from the day\n\n"
        "Weekly: One activity purely for fun, one social interaction, review your week\n\n"
        "The goal isn't perfection - it's consistency in small habits."
    ),

    # Thanks
    'thanks': "You're welcome! 💚 Remember, taking care of your mental health is just as important as your studies. You've got this!",
    'thank you': "Happy to help! 😊 Don't hesitate to come back anytime you need support. Take care of yourself!",
    'bye': "Take care! 💚 Remember - small steps every day. You're stronger than you think. Goodbye!",
}

DEFAULT_RESPONSES = [
    "I want to help! Could you tell me more about what you're going through? You can ask about stress, sleep, anxiety, exam tips, focus, loneliness, or type 'helpline' for emergency contacts.",
    "I didn't quite catch that. Try asking about: stress relief, sleep tips, anxiety, exam stress, focus, motivation, or helplines.",
    "I'm here to support you. Could you share a bit more? Common topics I help with: stress, anxiety, sleep, studies, focus, loneliness, depression.",
]

_default_index = 0

def format_response(text):
    """Convert markdown-like syntax to HTML for display in chat."""
    import re
    # Bold: **text** -> <b>text</b>
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    # Numbered lists: lines starting with "1. ", "2. " etc
    lines = text.split('\n')
    result = []
    for line in lines:
        stripped = line.strip()
        if re.match(r'^\d+\.\s', stripped):
            result.append(f'<li>{re.sub(r"^\\d+\\.\\s", "", stripped, count=1, flags=re.MULTILINE).lstrip()}')
            result[-1] = f'<li>{re.sub(r"^[0-9]+\.\s", "", stripped)}</li>'
        elif stripped.startswith('- '):
            result.append(f'<li>{stripped[2:]}</li>')
        elif stripped == '':
            result.append('<br>')
        else:
            result.append(stripped)
    # Wrap consecutive <li> in <ol> or <ul>
    html = ''
    i = 0
    while i < len(result):
        if result[i].startswith('<li>'):
            # collect all consecutive li
            block = []
            while i < len(result) and result[i].startswith('<li>'):
                block.append(result[i])
                i += 1
            html += '<ul style="margin:6px 0 6px 16px;padding:0">' + ''.join(block) + '</ul>'
        else:
            html += result[i] + ' '
            i += 1
    return html.strip()

def get_response(user_input):
    global _default_index
    text = user_input.lower().strip()

    sorted_keys = sorted(RESPONSES.keys(), key=len, reverse=True)
    for keyword in sorted_keys:
        if keyword in text:
            return format_response(RESPONSES[keyword])

    reply = DEFAULT_RESPONSES[_default_index % len(DEFAULT_RESPONSES)]
    _default_index += 1
    return "SHOW_QUICK|" + format_response(reply)  # special marker