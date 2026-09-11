#!/bin/bash
cd "$HOME/monetyzacja"
git init 2>/dev/null || true
git add .
git commit -m "Monetyzacja — start" 2>/dev/null || true
echo ""
echo "🌐 OPCJE PUBLIKACJI:"
echo ""
echo "A) GitHub Pages:"
echo "   1. https://github.com/new — załóż repo"
echo "   git remote add origin https://github.com/TWOJA/REPO.git"
echo "   git push -u origin main"
echo "   Settings → Pages → main / root"
echo ""
echo "B) Netlify (drag & drop):"
echo "   https://app.netlify.com/drop — przeciągnij folder"
echo "   Przeciągnij: ~/monetyzacja/portfolio"
echo ""
echo "C) Vercel:"
echo "   npx vercel --prod ~/monetyzacja/portfolio"
echo ""
echo "D) Lokalny test:"
echo "   python3 -m http.server 8080 --directory ~/monetyzacja"
echo "   Otwórz: http://localhost:8080"
