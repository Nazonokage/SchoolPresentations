from pathlib import Path
import re, shutil
base = Path(__file__).resolve().parents[2]
def edit(relative, transform):
    path = base / relative
    path.write_text(transform(path.read_text(encoding='utf-8')),encoding='utf-8')

# Make M01's first-hands-on target match the code and remove repeated scaffold blocks.
def refine1(text):
    text = text.replace('and add one package', 'and trace a baon calculation')
    text = text.replace('the phone shows "Hello, ADET!" after you save, without reinstalling anything.', 'the app displays a greeting and the calculated balance after your edit.')
    text = re.sub(r'\*\*Run it\.\*\*\n\n```powershell\n.*?\n```', '**Run it.** Copy the complete App.tsx below into that project, then repeat `npx tsc --noEmit` and start Expo. The type check must happen after your code changes.', text, count=1, flags=re.S)
    text = text.replace('Install a matching Expo Go build from expo.dev/go, or recreate the project on the SDK your Expo Go supports.', 'Ask the instructor to check the actual client against the SDK 58 baseline using expo.dev/go. Physical iOS devices cannot be assumed to install arbitrary older Expo Go versions. Do not change the course SDK independently.')
    text = text.replace('Run `npx expo install <name>` and restart.', 'For this core checkpoint, check the import spelling and prepared dependencies first. Extra packages require online preparation, not an unplanned lab download.')
    text = text.replace('| M01–M03 | none beyond `react-native` | none | No |', '| M01–M03 | react and react-native from template | none | No |')
    return text
edit('modules/ADET_M01.md',refine1)

# Add an explicitly optional extension preserving the absorbed form/effect topic.
source=(base/'examples/M03/App.tsx').read_text(encoding='utf-8')
timeout=source.replace('import { useState }','import { useEffect, useState }')
timeout=timeout.replace('  function handleLogin()', '''  useEffect(() => {
    if (message === "") return; // No feedback means nothing to schedule.
    const timeoutId = setTimeout(() => setMessage(""), 4000);
    return () => clearTimeout(timeoutId); // Cancel old work before the next message or removal.
  }, [message]);

  function handleLogin()''')
(base/'examples/M03/App.timeout.tsx').write_text(timeout,encoding='utf-8')
def refine3(text):
    extra='''### Optional ungraded comparison — feedback that clears

Old M04's message-dependent timer now belongs here, connected to M02's effect cleanup. The complete [App.timeout.tsx](../examples/M03/App.timeout.tsx) uses only template packages. Copy it as App.tsx in a spare starter copy and run the same type-check/start commands. It adds useEffect to the React import and a four-second timeout that clears nonempty feedback.

**Predict first:** submit a different message after two seconds. Which timeout should clear the new message? The old effect cleans up its timeout, then the new effect schedules one for the changed message. At roughly four seconds after that change, feedback clears. Submitting the identical message does not change state, so it does not restart this timer. A delay is a minimum scheduling request, not an accurate clock. This is a UI cleanup comparison, not an event-driven architecture lesson.

| Moment | Message | Resource |
|---|---|---|
| Start | empty | No timeout |
| Submit valid pair | Welcome, Virel! | Schedule A |
| Submit an empty username before A fires | Enter both username and password. | Cancel A; schedule B |
| B callback eventually runs | empty | Feedback cleared; effect no longer schedules work |

For keyboard dismissal, React Native's Keyboard.dismiss() can be called in the press handler; it is a built-in API, not validation. Keep it separate from the rule determining the message. More elaborate form libraries do not remove the need for server validation; they are outside this small core checkpoint.

'''
    return text.replace('## D. Assessment, Wrap-Up & References',extra+'## D. Assessment, Wrap-Up & References')
edit('modules/ADET_M03.md',refine3)

# Keep optional assets/theme discussion from old M03, while the assessed screen remains small.
def refine4(text):
    return text.replace('### Common mistakes', '''### Optional design comparison — assets and theme

An asset is a bundled file such as the starter's assets/icon.png. If you add Image from react-native, a local source such as `require("./assets/icon.png")` can work without an image server; the path is relative to App.tsx. Give it width/height and an accessibilityLabel when it conveys information. Decorative images should not create distracting duplicate announcements. No remote CDN is needed.

useColorScheme from react-native reports the preferred theme. A dark-theme extension chooses both foreground and background together, then checks contrast; changing only the background can hide text. Neither a theme hook nor a label automatically makes the whole screen accessible. These are optional ungraded design comparisons after the responsive core, not extra graded tasks.

### Common mistakes''')
edit('modules/ADET_M04.md',refine4)

for number in range(6):
    name=f'modules/ADET_M{number:02}.md'
    edit(name,lambda text: text.replace('keys and grading guidance are in the separate instructor folder.', 'keys and grading guidance are in [the separate instructor key](../instructor/OPENER_ANSWER_KEY.md).'))

# Preserve the inactive old Router files in the review backup, leaving mobile unambiguously App.tsx.
mobile=base/'examples/mobile'
archive=base/'instructor/stop2-2026-11-07/before/examples/mobile'
for path in (mobile/'app').rglob('*.tsx'):
    target=archive/path.relative_to(mobile)
    target.parent.mkdir(parents=True,exist_ok=True)
    if not target.exists(): shutil.copy2(path,target)
    path.unlink()
old=base/'examples/M05/[id].tsx'
if old.exists():
    old.unlink() # Original was already preserved by opener_support's save helper.
print('Refined explanations; preserved old timer comparison and isolated Router layout.')
