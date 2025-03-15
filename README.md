## Getting Started

### Prerequisites

Ensure you have the following installed on your local machine:

- Python 3.x
- pip (Python package installer)

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/hi-heavens/nexascale-python-task-1.git
   cd nexascale-python-task-1
   ```

2. Install the required Python libraries:

   ```sh
   pip install psutil requests python-dotenv
   ```

3. Create a `.env` file in the root directory and add your OpenWeatherMap API key:
   ```env
   API_KEY=your_openweathermap_api_key
   ```

### Usage

#### 1. System Monitoring Script

Run the system monitoring script to display CPU and memory usage:

```sh
python3 01-monitor-script.py
```

#### 2. API Interaction (Weather Data Fetching)

Fetch weather data for a given city:

```sh
python3 02-weather-data.py
```

#### 3. Log File Error Scanner

Scan a log file for occurrences of the word "ERROR":

```sh
python3 03-log-scanner.py
```

### Example Outputs

#### System Monitoring Script

```
CPU Usage: 17.5% Memory Usage: 69.7
```

#### API Interaction (Weather Data Fetching)

```
Weather in Lagos: Temperature: 32.52°C Condition: light rain Humidity: 58%
Weather in Nairobi: Temperature: 28.72°C Condition: few clouds Humidity: 26%
```

#### Log File Error Scanner

```
Found 6 occurrences of 'ERROR' in logs.
```

### Bonus Features

- **System Monitoring Script**: Logs CPU and memory usage data into a file for future analysis called 'monitoring-log.txt'.
- **API Interaction**: Allows you to enter multiple city names to fetch weather data.
- **Log File Error Scanner**: Filters logs by date or severity level (INFO, WARNING, ERROR).

### Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

### Author

Olaitan Adedokun - [hi-heavens](https://github.com/hi-heavens/)
