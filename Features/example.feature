Feature: Smoke Test for Ethereum Blockchain

  Scenario: Basic functionality check
    Given I am connected to 1 Ethereum node
    When I send a simple transaction
    Then the transaction should be mined successfully
    And the block should be added to the blockchain