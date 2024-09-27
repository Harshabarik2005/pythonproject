import subprocess

def scan_docker_image(image_name):
    try:
        # Step 1: Pull the Docker image
        print(f"Pulling Docker image: {image_name}")
        subprocess.run(["docker", "pull", image_name], check=True)

        # Step 2: Scan the Docker image with Trivy
        print(f"Scanning Docker image: {image_name} for vulnerabilities...")
        result = subprocess.run(["trivy", "image", image_name], capture_output=True, text=True)
        
        # Step 3: Output the scan result
        print(result.stdout)

        # Step 4: Check for critical vulnerabilities
        if "CRITICAL" in result.stdout:
            print(f"Critical vulnerabilities found in image {image_name}.")
            return False
        else:
            print(f"No critical vulnerabilities found in image {image_name}.")
            return True

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while pulling or scanning the image: {e}")
        return False

if __name__ == "__main__":
    # Specify the Docker image name you want to scan
    image_name = "nginx:latest"

    # Run the scan and get the result
    scan_successful = scan_docker_image(image_name)

    if not scan_successful:
        print("Scan failed or vulnerabilities detected.")
        exit(1)
    else:
        print("Scan completed successfully. No critical vulnerabilities found.")
