@cucumber-basket
Feature: Cucumber Basket
  As a gardener,
  I want to carry cucumbers in a basket,
  So that I don't drop them all

  @add
  Scenario Outline: Add cucumbers to a basket
    Given the basket has "<initial>" cucumbers
    When "<some>" cucumbers are added to the basket
    Then the basket contains "<total>" cucumbers

    Examples: Amount of cucumbers
      | initial | some | total |
      | 2       | 4    | 6     |
      | 0       | 3    | 3     |
      | 5       | 5    | 10    |

  @remove
  Scenario: Remove cucumbers from the basket
    Given the basket has "6" cucumbers
    When "4" cucumbers are removed from the basket
    Then the basket contains "2" cucumbers