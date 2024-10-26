# 🍌 ApesUnchained Website: Where Monkeys Go Bananas for Code! 🐒

Welcome to the ApesUnchained website repository! We're not monkeying around when it comes to building awesome static sites. Our custom Python-based generator is so efficient, it'll make you go ape!

## 🐵 Getting Started: No Monkey Business Here!

Before you start swinging through our code jungle, make sure you've got your banana peeler (Git) ready and your coconut shell (terminal) open. Let's go bananas!

1. Clone this repository faster than a chimp can peel a banana:
   ```
   git clone https://github.com/mon-key-mike/ApesUnchained.git
   cd ApesUnchained
   ```

2. Install the required dependencies (no banana-flavored packages, sorry):
   ```
   pip install markdown jinja2
   ```

3. Build the site (watch the magic happen faster than a monkey can throw... well, you know):
   ```
   python makesite.py
   ```

4. The generated site will appear in the `_site` directory like magic (or like a banana suddenly appearing in your hand). Serve it locally using this simple incantation:
   ```
   python -m http.server -d _site
   ```

   Then swing over to `http://localhost:8000` in your favorite browser (Gorilla Chrome, anyone?).

## 🍌 Adding Content: Feed the Code Monkey

Want to add new pages? It's easier than teaching a monkey to use a smartphone! Just create Markdown files in the `content` directory. Our site is smarter than the average ape - it'll automatically rebuild and deploy when you push changes to the `main` branch. It's so easy, even a monkey could do it! (No offense to our primate friends, of course.)

## 🙈 Customizing: Dress Your Monkey in Style

- Monkey see, monkey do: Modify the layouts in the `layout` directory to change the site's structure.
- Give your site some banana-yellow flair: Update the CSS in `static/css/style.css`.
- Teach your site some new tricks: Add JavaScript functionality in `static/js/main.js`.

## 🚀 Deployment: Launching Monkeys into Cyberspace

Our site deploys faster than a monkey can climb a tree! The GitHub Actions workflow in `.github/workflows/deploy.yml` handles the build and deployment process. It's so smooth, it's like sliding down a banana peel!

## 🍌 The Banana-Bunch Behind the Scenes

Our `makesite.py` file is the top banana of this operation. It's got more features than a Swiss Army banana:

- Jinja2 templating: Because even monkeys deserve fancy templates.
- Markdown parsing: Turn your monkey scribbles into beautiful HTML.
- JSON data loading: Store your bananas... I mean, data... in easy-to-manage files.
- Date-based sorting: Keep your content fresher than a just-peeled banana.

## 🐒 Contributing: Join Our Monkey Business!

We're always looking for more cool cats (or should we say, cool primates?) to join our tree house. If you've got a bunch of great ideas, don't go ape - just follow these steps:

1. Fork the repository (it's like stealing a banana, but legal).
2. Create your feature branch: `git checkout -b feature/BananaPhone`
3. Commit your changes: `git commit -am 'Add some BananaPhone'`
4. Push to the branch: `git push origin feature/BananaPhone`
5. Submit a pull request (and maybe a banana or two for good measure).

## 📜 License: The Banana Republic Constitution

This project is open source and available under the MIT License. In other words, it's free-er than a monkey in the jungle!

## 🍌 Final Words: May the Fork Be With You!

Remember, in the world of coding, every bug is just a chance to go bananas and find creative solutions. So keep calm and monkey on!

Now go forth and create a website so amazing, it'll make King Kong look like a chimp-anzee!

*P.S. If you've read this far, you deserve a banana. 🍌 Here, have a virtual one!*
