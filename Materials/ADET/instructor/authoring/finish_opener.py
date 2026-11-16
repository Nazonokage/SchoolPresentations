from pathlib import Path
import re
base=Path(__file__).resolve().parents[2]
for number in range(6):
    path=base/f'modules/ADET_M{number:02}.md'
    text=path.read_text(encoding='utf-8')
    if number==1:
        text=re.sub(r'> \*\*Course baseline.*?\n', '> **Tested course baseline — November 6–7, 2026:** Expo SDK 58 (expo 58.0.23), React Native 0.88.1, React 19.3.0, TypeScript 6.0.3, Node 24.18.1 and npm 11.16.0. Use the prepared starter and lockfile. Local compilation/bundling passed; native-device and phone-network checks remain pending.\n',text,count=1)
        text=text.replace('> The **default** template uses file-based routing and its first screen is `src/app/index.tsx`, with no `App.tsx`.', '> A Router-based template uses route files rather than this course\'s App.tsx entry.')
        text=text.replace('**Install first.**', '**Real-world use case.** A student checks whether today\'s baon covers two purchases. The screen explains a shortage instead of treating a negative number as a crash.\n\n**Install first.**',1)
        text=text.replace('### Instructor notes\n', '### Instructor notes\n\nEnvironment evidence: [stop-1 report](../instructor/stop1-2026-11-06/REPORT.md). SDK support was checked using store metadata separately from create-expo-app; --no-agents-md succeeded for both tested templates. The optional expo-constants exploration is not assessed.\n')
    if number in [1,2,3]:
        table='''### Core dependency check

| Import / tool | Prepared source | Extra install / permission / plugin |
|---|---|---|
| react | Blank template; component state/effects where used | None |
| react-native | Blank template; native views and built-in APIs | None |
| TypeScript / Expo CLI | Prepared dev toolchain | None during offline class |

Core entry: index.ts → App.tsx. Compatible Expo Go can host these APIs; perform the actual native-client smoke test before class. This does not certify the phone/network route.

'''
        text=text.replace('**Install first.**',table+'**Install first.**',1)
    if number in [0,1,2,3]:
        timings = ('5 introduction, 20 explanation, 15 paper practice, 15 quiz, 5 wrap-up' if number==0 else '5 review, 15 explanation, 10 guided program, 25 individual activity, 5 wrap-up' if number in [1,3] else '5 review, 20 explanation/trace, 15 demonstration, 15 quiz, 5 wrap-up')
        text=text.replace('### Instructor notes\n','### Instructor notes\n\n**60-minute pacing:** '+timings+'. Use the additional 30 minutes for support and deeper traces, not another graded task.\n')
    if number in [1,3,4]:
        text=text.replace('### Before next meeting — laptop preparation announcement',f'### Before next meeting — M{number:02} preparation handout (send before this lesson)',1)
    # Keep instructor notes separate from prose and lists with proper CommonMark spacing.
    text=text.replace('\n**Teaching evidence:**','\n\n**Teaching evidence:**')
    path.write_text(text,encoding='utf-8')

print('Finished student/instructor separation, setup tables and pacing.')
