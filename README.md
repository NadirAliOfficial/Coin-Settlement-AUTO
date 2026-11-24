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
python auto.py
```

## Config

```env
WALLET_ADDRESS=your_wallet
API_KEY=your_exchange_api_key
MIN_SETTLEMENT=0.001
CHECK_INTERVAL=30
```

## Requirements

No external Python packages are required beyond the standard library.

## Installation

1. Clone the repository.
2. Ensure you have Python 3 installed.
3. Run the main script:
   ```bash
   python auto.py
   ```

## Usage

Execute `auto.py` to start the settlement loop. The script will use the configuration values defined in the `.env` file.

## Project Structure

| File | Description |
|------|-------------|
| `auto.py` | Main settlement loop |
| `Coin Updated.py` | Core settlement logic |
| `ErrorHnadling.py` | Error recovery handler |
| `tweet.py` | Twitter notification on events |

## Files

| File | Description |
|------|-------------|
| `auto.py` | Main settlement loop |
| `Coin Updated.py` | Core settlement logic |
| `ErrorHnadling.py` | Error recovery handler |
| `tweet.py` | Twitter notification on events |
