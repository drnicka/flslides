# #VOICE Presentation

This repository contains the presentation slides for #VOICE, built using mkslides and reveal.js.

## How It Works

1. **Markdown with HTML Templates**: Create slides in markdown with reveal.js-compatible HTML:
```html
<!-- Example slide -->
<section>
  <h1 style="font-size: 3em;">#VOICE</h1>
  <p style="font-size: 1.4em;">An Application for Preference Signaling</p>
  <img src="logo.png" alt="Logo" style="max-width: 450px;">
</section>
```

2. **Build Process**: mkslides converts markdown to a static HTML presentation:
```bash
# Build the presentation
mkslides build markdown_files/ScrollVoice1.md

# Preview locally
mkslides serve markdown_files/ScrollVoice1.md
```

3. **Deployment**: Push to GitHub Pages using the workflow:
```bash
# After making changes
git add markdown_files/ScrollVoice1.md
git add site/     # Contains the built HTML and assets
git commit -m "Update presentation content"
git push origin main
```

## Project Structure

```
mkslides_project/
├── markdown_files/
│   └── ScrollVoice1.md    # Main presentation source
├── site/
│   ├── index.html         # Built presentation
│   ├── assets/            # reveal.js assets
│   └── *.{png,jpg}       # Images
└── .github/
    └── workflows/
        └── pages.yml      # GitHub Pages deployment
```

## Live Presentation

View the live presentation at: https://drnicka.github.io/flslides/

## Local Development

1. **Setup**:
```bash
pip install -r requirements.txt
```

2. **Development Workflow**:
   - Edit `markdown_files/ScrollVoice1.md`
   - Run `mkslides serve markdown_files/ScrollVoice1.md` for live preview
   - Make changes and refresh browser to see updates

3. **Build & Deploy**:
   - Build: `mkslides build markdown_files/ScrollVoice1.md`
   - Commit and push changes
   - GitHub Actions will automatically deploy to Pages

## Notes
- The presentation uses reveal.js for rendering slides
- Images should be placed in the `site/` directory
- Custom styles can be added directly in the markdown using HTML and CSS
