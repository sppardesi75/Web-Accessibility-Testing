from selenium import webdriver
import json
import time

# Axe-core CDN link
AXE_JS_URL = "https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.4.2/axe.min.js"

def run_accessibility_test(url):
    # Set up WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(3)  # Wait for page to fully load

        # Inject axe-core JavaScript into the page
        driver.execute_script(f"""
            var script = document.createElement('script');
            script.src = '{AXE_JS_URL}';
            script.async = false;
            document.head.appendChild(script);
        """)
        time.sleep(2)  # Give some time for axe-core to load

        # Run axe accessibility scan
        axe_results = driver.execute_script("return axe.run()")
        driver.quit()

        # Save results to a JSON file
        with open("accessibility_report.json", "w") as file:
            json.dump(axe_results, file, indent=4)
        
        print("Accessibility test completed. Report saved as 'accessibility_report.json'.")

    except Exception as e:
        print(f"Error: {e}")
        driver.quit()

# Test Example
if __name__ == "__main__":
    test_url = "https://www.senecacollege.ca/"
    run_accessibility_test(test_url)
