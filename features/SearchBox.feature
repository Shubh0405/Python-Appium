Feature: Search Box

    Scenario: User goes inside electronics category and searchs for iphone
    Given Flipkart app opens
    And English Language Selected
    And login flow skipped
    When category page opens 
    Then Click on the seach icon and enter text iphone
    And close app