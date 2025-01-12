# Strawpoll Vote Generator

This script automates the process of voting on a poll hosted on Strawpoll. It uses Python's `requests` library to interact with the poll's API and `threading` to run multiple voting threads simultaneously. The script is configured through a `config.json` file to allow for flexibility in voting parameters.

## Features
- **Automated Voting**: Cast votes programmatically on a specific poll item.
- **Multi-threading Support**: Speeds up the voting process by running multiple threads.
- **Customizable Configuration**: Control poll URL, item to vote for, thread count, and vote count via `config.json`.

## Prerequisites
1. **Python**: Make sure you have Python 3.7 or later installed.
2. **Dependencies**: Install the required Python packages:
   ```bash
   pip install requests

# Configuration File (`config.json`)

The `config.json` file allows you to customize the behavior of the voting script. You can modify values such as the poll URL, the item you want to vote for, the number of threads, and how many votes each thread should cast.

---

## Configuration Parameters

### 1. `poll_url`
- **Type**: `String`
- **Description**: The URL of the Strawpoll you want to automate voting for.
- **Example**: 
  ```json
  "poll_url": "https://strawpoll.com/bVg8BpG5ByY"
  ```
### 2. `item_name`
- **Type**: `String`
- **Description**: The name of the item/option to vote for in the poll. Ensure this matches exactly with the option's name on the poll.
- **Example**: 
  ```json
  "item_name": "Item1"
  ```
### 3. `threads_count`
- **Type**: `Integer`
- **Description**: The number of threads to use for concurrent voting. More threads will result in faster voting, but may cause higher server load.
- **Example**: 
  ```json
  "threads_count": 1
  ```
### 4. `vote_count`
- **Type**: `Integer`
- **Description**: The number of votes each thread should cast. This determines how many votes a single thread will contribute to the poll.
- **Example**: 
  ```json
  "vote_count": 10
  ```
## Usage

## 1. Clone the Repository

First, clone the repository to your local machine:

```
git clone https://github.com/your-username/Strawpoll-Vote-Generator.git && cd Strawpoll-Vote-Generator 
```
---

## 2. Install Dependencies

Make sure you have Python 3.7 or above installed. Install the required dependencies by running:
```
pip install requests
```
This will install the necessary Python libraries for the script to function.

---

## 3. Configure `config.json`

Before running the script, you need to modify the `config.json` file. This file contains all the configurable parameters such as the poll URL, item name, and voting settings.

- Open the `config.json` file.
- Update the following fields:
  - **`poll_url`**: The URL of the Strawpoll you want to automate voting for.
  - **`item_name`**: The name of the item you want to vote for in the poll.
  - **`threads_count`**: The number of threads to run concurrently (default: 1).
  - **`vote_count`**: The number of votes each thread should cast (default: 10).

Example configuration:

```json
{
  "poll_url": "https://strawpoll.com/bVgGGpN7ByY",
  "item_name": "Item1",
  "threads_count": 1,
  "vote_count": 10
}
```

## 4. Run the script
Once you have configured the config.json file, run the script using Python:
```
python req.py
```
This will start the automated voting process. The script will use the configuration in config.json to vote for the selected item multiple times, leveraging multi-threading for faster execution.

# Notes

This section provides additional information and important considerations when using the script.

---

## Rate Limiting
- Sending too many requests in a short time may trigger rate-limiting or result in your IP being temporarily banned from the poll platform.
- Use the script responsibly and avoid excessive use to prevent service disruptions.

---

## Poll URL and Item Name Accuracy
- Ensure that the **`poll_url`** in the `config.json` file is correct and points to the intended Strawpoll.
- The **`item_name`** should match exactly with the name of the option you want to vote for. Any typo or mismatch could lead to failed votes.

---

## Script Termination
- If you wish to stop the script at any point, simply press `Ctrl+C` in your terminal. This will terminate the process gracefully.

---

## Customization
- You can adjust the number of threads (`threads_count`) and votes per thread (`vote_count`) in the `config.json` file to customize the script's performance based on your needs.
- Be mindful of the number of threads you use, as more threads can increase the load on the target server and cause it to respond slower or block further requests.

---

## Legal and Ethical Considerations
- Automating votes on platforms such as Strawpoll may violate the site's terms of service. Always read and adhere to the platform's rules and guidelines.
- Use the script responsibly, keeping in mind the ethical implications of automating votes and the potential impact on other users.

---

By following these notes, you can ensure that the script works as intended while avoiding common pitfalls.


## License

[MIT](https://choosealicense.com/licenses/mit/)
