Tired of flaky tests due to unavailable Sauce Connect tunnels?

This project helps you ensure your tests only run when a Sauce Connect tunnel is fully established, preventing the "No active tunnel" error entirely.

Why is this useful?

Eliminate wasted time: Don't let your tests fail and retry because of a missing tunnel.
Focus on reliable results: Only run tests when the environment is ready, leading to more consistent outcomes.

How does it work?

This example is made up of three scripts:
1. The Selenium test script named "test_chrome_latest.py" which returns the version number of the Chrome browser when using the "latest" capability.
2. The script named "tunnel_check.py" utilizes the Requests module to query the Sauce Labs Tunnel API to ensure that the tunnel is available prior to executing the test script.
3. Lastly, the "run.py" script is the script that you will execute. It first makes a call to "tunnel_check.py" and upon a successful exit code it will then execute "test_chrome_latest.py".


