# AI Virtual Assistant for Agency

This is an n8n workflow for an **AI Virtual Assistant** that uses natural language to schedule meetings via Telegram, checks Google Calendar for availability, cross-references contacts in Google Sheets, and sends confirmation emails.

## 📸 Workflow Overview

This repository contains the workflow for the n8n automation platform. Below is a visual representation of the workflow:

![Workflow Diagram](./new-image.png)

The workflow includes the following nodes:

1. **Telegram Trigger**: Listens for incoming messages on Telegram.
2. **Prepare Data**: Processes the incoming data.
3. **OpenAI Model**: Utilizes AI to process and analyze the data.
4. **Load CRM Data**: Reads data from the CRM.
5. **CRM Search Tool**: Searches the CRM for relevant information.
6. **Google Calendar Tool**: Creates calendar events.
7. **Send Response**: Sends a response back to the user.
8. **Send Confirmation Email**: Sends a confirmation email for the created event.

## 📋 Features
- **Natural language interface:** Chat via Telegram
- **Autonomous execution:** GPT-4o decides on available time slots
- **Context-aware:** Uses CRM lookup (Google Sheets) and Availability check (Google Calendar)
- **Easy scheduling:** Auto-sends Google Calendar invites and Gmail confirmations

## 🚀 Setup & Usage
1. Import \i-assistant.json\ into your n8n workspace.
2. Configure credentials:
   - **Telegram:** Add your Bot Token.
   - **OpenAI:** Add your API Key.
   - **Google Sheets & Calendar:** Connect your Google account.
3. Activate the workflow and chat with your bot!

## Tech Stack
- n8n
- Telegram
- OpenAI (gpt-4o)
- Google Workspace (Sheets, Calendar, Gmail)
