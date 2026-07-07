# Coin Settlement Auto

Automated cryptocurrency settlement workflow — monitors wallet balances, processes pending settlements, and handles error recovery.

## Features

- Auto-detect incoming transactions
- Settlement queue with retry logic
- Error handling and logging
- Configurable thresholds and intervals
- Tweet notifications on settlement events

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env  # Add your API keys
python auto.py
```

## Config

```env
WALLET_ADDRESS=your_wallet
API_KEY=your_exchange_api_key
MIN_SETTLEMENT=0.001
CHECK_INTERVAL=30
```

## Files

| File | Description |
|------|-------------|
| `auto.py` | Main settlement loop |
| `Coin Updated.py` | Core settlement logic |
| `ErrorHnadling.py` | Error recovery handler |
| `tweet.py` | Twitter notification on events |
