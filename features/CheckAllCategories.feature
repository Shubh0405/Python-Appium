Feature: All Categories

    Scenario: Check All Categories check
        Given Flipkart app opens
        And English Language Selected
        And login flow skipped
        When category page opens
        Then Verify all categories text
        And close app