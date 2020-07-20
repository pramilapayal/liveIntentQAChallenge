@validateStreamData

  Feature: Verify the data is passed in appropriate stream based on the seed value passed by the user
    Scenario Outline: As a user when I send odd number or even number then message is sent to li-stream-even stream or li-stream-odd stream respectively
      Given livestream is up and running
      When I send data in route for <seedvalue> and validate <expectedResults>
      Then I should get data in li-stream-even stream when even number is passed as seedvalue and li-stream-odd stream when odd number is passed as <seedvalue>
      Examples:
      |seedvalue    |expectedResults|
      |3            |200            |
      |2            |200            |
      |invalid      |400            |
      |             |404            |
