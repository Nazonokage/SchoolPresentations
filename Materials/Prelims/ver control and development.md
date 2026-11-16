# Git, GitHub & Vercel — Intro Deck Flow (v2)

## 1. Title Slide
- Title: "From Code to Cloud: Git, GitHub & Vercel"
- Subtitle: "Version control to live deployment"
- Presenter name / date

## 2. Agenda
- What is Git? (+ analogy, alternatives)
- What is GitHub? (+ analogy, alternatives)
- What is Vercel? (+ analogy, alternatives)
- How they work together
- Live demo / workflow recap

## 3. The Problem (Hook Slide)
- Working without version control: overwritten files, "final_v2_FINAL.docx" chaos
- No easy collaboration or rollback
- Sets up "why do we need this?"

## 4. What is Git?
- Definition: distributed version control system
- Tracks changes to code over time
- Key concepts: repository, commit, branch, merge

## 5. Analogy Slide — Git
- Like "Track Changes" in Word/Google Docs, but for entire projects
- Or: a save-game system in video games — checkpoints you can return to anytime
- Or: a time machine for your codebase — jump to any past version

## 6. Similar Tools to Git (Familiarity Slide)
- Mercurial (Hg) — another distributed VCS, less common now
- SVN (Subversion) — older, centralized version control
- Perforce — used heavily in game dev / large binary files
- Takeaway: Git won the popularity contest — it's the industry standard today

## 7. Core Git Commands (Quick Reference)
- `git init`, `git add`, `git commit`
- `git branch`, `git checkout`/`git switch`
- `git merge`, `git pull`, `git push`
- Keep it visual (icons/flow arrows), not a wall of text

## 8. Git Workflow Diagram
- Visual: working directory → staging area → local repo → remote repo
- Helps visualize commit lifecycle

## 9. What is GitHub?
- Definition: cloud hosting platform for Git repositories
- Git = tool, GitHub = platform/service built around it
- Key features: remote repos, collaboration, pull requests, issues

## 10. Analogy Slide — GitHub
- Like Google Drive for your Git repos — cloud storage + sharing + collaboration
- Or: a social network for code — profiles, following, stars, contributions
- Git is the engine, GitHub is the garage where everyone works on the car together

## 11. Similar Tools to GitHub (Familiarity Slide)
- GitLab — similar features, popular for self-hosting & built-in CI/CD
- Bitbucket — Atlassian's version, integrates with Jira/Trello
- Takeaway: same core idea (host + collaborate on Git repos), different ecosystems

## 12. Git vs GitHub (Clarify Common Confusion)
- Simple comparison table
- Git = local version control
- GitHub = online collaboration + hosting

## 13. GitHub Features Overview
- Pull Requests & Code Review
- Issues & Project boards
- Actions (CI/CD)
- GitHub Pages (bonus mention)

## 14. Typical Team Workflow
- Clone repo → create branch → commit changes → push → open PR → review → merge

## 15. What is Vercel?
- Definition: cloud platform for frontend deployment & hosting
- Built for modern frameworks (Next.js, React, etc.)
- Zero-config deployments, instant previews

## 16. Analogy Slide — Vercel
- Like a restaurant that plates and serves your food the moment it's cooked — you just cook (code), Vercel serves it to the world
- Or: a vending machine for websites — push code in, get a live URL out
- Or: valet parking for your app — hand over the keys (code), it handles the rest (build, host, scale)

## 17. Similar Tools to Vercel (Familiarity Slide)
- Netlify — very similar, strong for static sites & JAMstack
- AWS Amplify — more infrastructure control, steeper learning curve
- Railway / Render — broader hosting (backend + databases too)
- GitHub Pages — free but limited to static sites
- Takeaway: Vercel stands out for its Git integration + speed + Next.js synergy

## 18. Why Vercel? (Key Benefits)
- Git integration (auto-deploy on push)
- Preview deployments for every branch/PR
- Global CDN, fast builds
- Free tier for personal projects

## 19. The Full Workflow (Big Picture Slide)
- Visual flow: 
  Code locally (Git) → Push to GitHub → Vercel auto-deploys → Live site
- This is the "aha" slide tying everything together

## 20. Live Demo (Optional but Powerful)
- Create a repo → push code → connect to Vercel → see live deployment
- Show a Pull Request triggering a preview deployment

## 21. Common Use Cases
- Personal portfolio sites
- Team projects with CI/CD
- Open source collaboration

## 22. Recap Slide
- Git = version control (the time machine)
- GitHub = collaboration & hosting (the shared garage)
- Vercel = deployment & hosting for the web (the valet)
- Together = full dev-to-production pipeline

## 23. Q&A / Thank You Slide
- Contact info / resources
- Links: git-scm.com, github.com, vercel.com