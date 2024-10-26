# ApesUnchained: Discord-Powered Static Site Generator

## Setting Up Discord Webhook

1. In your Discord server, go to Server Settings > Integrations > Webhooks.
2. Click "New Webhook" and configure it for the channel you want to use.
3. Copy the Webhook URL.

## Configuring GitHub for Discord Webhooks

1. Go to your GitHub repository settings.
2. Navigate to "Secrets and variables" > "Actions".
3. Add a new repository secret named `DISCORD_WEBHOOK_SECRET`.
4. Set its value to a secure random string. This will be used to verify webhook requests.

## Setting Up the Discord-to-GitHub Bridge

To securely bridge Discord webhooks to GitHub Actions, you'll need a small server to verify and forward the webhooks. Here's a simple Express.js server you can deploy (e.g., on Heroku):

```javascript
const express = require('express');
const crypto = require('crypto');
const axios = require('axios');

const app = express();
app.use(express.json());

const DISCORD_WEBHOOK_SECRET = process.env.DISCORD_WEBHOOK_SECRET;
const GITHUB_PERSONAL_ACCESS_TOKEN = process.env.GITHUB_PERSONAL_ACCESS_TOKEN;
const GITHUB_REPO = 'your-username/your-repo-name';

app.post('/webhook', (req, res) => {
  const signature = req.get('X-Signature-Ed25519');
  const timestamp = req.get('X-Signature-Timestamp');
  const body = JSON.stringify(req.body);

  const isVerified = verifyDiscordRequest(DISCORD_WEBHOOK_SECRET, signature, timestamp, body);
  if (!isVerified) {
    return res.status(401).send('Invalid signature');
  }

  // Forward to GitHub
  axios.post(`https://api.github.com/repos/${GITHUB_REPO}/dispatches`, {
    event_type: 'discord-webhook',
    client_payload: req.body
  }, {
    headers: {
      'Authorization': `token ${GITHUB_PERSONAL_ACCESS_TOKEN}`,
      'Accept': 'application/vnd.github.v3+json'
    }
  }).then(() => {
    res.status(200).send('Webhook processed');
  }).catch(error => {
    console.error('Error forwarding to GitHub:', error);
    res.status(500).send('Error processing webhook');
  });
});

function verifyDiscordRequest(clientPublicKey, signature, timestamp, body) {
  try {
    const message = timestamp + body;
    const verified = crypto.verify(
      'ed25519',
      Buffer.from(message),
      clientPublicKey,
      Buffer.from(signature, 'hex')
    );
    return verified;
  } catch (err) {
    console.error('Error verifying request:', err);
    return false;
  }
}

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
