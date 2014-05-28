Feature: Confirming that the tip calculator form works

    Scenario: check that the form displays
        When I go to the tip calculator
        Then I should see the calculator form

    Scenario: check that the form submits successfully
		When I go to the tip calculator
		And I submit the form with a valid total and tip percentage
		Then I should see the results page

	Scenario: check that the application calculates the tip correctly
		When I go to the tip calculator
		And I submit the form with a total of 50 and a tip percentage of 20
		Then I should see a tip result of 10
