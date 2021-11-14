# OSC-API

<p align="center">
        <img src="https://i.pinimg.com/originals/72/10/78/721078d6b03e349cea9e59f24b42420c.png" width=500>
    <br>AMS - ASSIGNMENT MANAGEMENT SYSTEM
</p>

## API Endpoints

| ID  | Endpoint              | Example                                    | Details                                           |
| --- | --------------------- | ------------------------------------------ | ------------------------------------------------- |
| 1   | [/]                   | https://osc-api.herokuapp.com/             | Index.                                            |
| 1   | [/api/]               | https://osc-api.herokuapp.com/api/         | API Base endpoint with documentation              |
| 2   | [api/event/]          | https://osc-api.herokuapp.com/event/       | GET complete data on all the events.              |
| 3   | [api/event/\<int:id>] | https://osc-api.herokuapp.com/event/8      | GET data from a particular event (from Event ID). |
| 4   | [api/event/latest]    | https://osc-api.herokuapp.com/event/latest | GET data of the latest OSC event.                 |
