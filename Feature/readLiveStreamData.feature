@validateStreamData

  Feature: Verify the data is passed in appropriate stream based on the seed value passed by the user
    Scenario Outline: As a user when I send odd number or even number then message is sent to li-stream-even stream or li-stream-odd stream respectively
      Given livestream is up and running
      When I send data in route for <seed_value> and validate <expected_results>
      Then I should get data in <stream_name> depending on the <seed_value>
      Examples:
      |seed_value            |expected_results |stream_name         |
      |1242                  |200              |li-stream-even      |
      |333                   |200              |li-stream-odd       |
      |                      |404              |li-stream-even      |
      |0                     |200              |li-stream-even      |
      |invalid               |400              |li-stream-even      |
      |0.01                  |400              |li-stream-even      |
      |21474836482147422211  |400              |li-stream-even      |
      |21474836482147422211  |400              |li-stream-odd       |
      |-0.1                  |400              |li-stream-even      |
