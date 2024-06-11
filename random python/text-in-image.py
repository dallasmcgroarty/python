import cv2
import pytesseract

def find_text_in_image(query, image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Use pytesseract to extract text from the image
    extracted_text = pytesseract.image_to_string(gray)
    
    # Check if the query string is present in the extracted text
    if query.lower() in extracted_text.lower():
        return True
    else:
        return False

# Example usage
query_string = "pig"
image_file = "farm-animals.jpg"  # Change this to the path of your image file
result = find_text_in_image(query_string, image_file)
print("Is '{}' present in the image? {}".format(query_string, result))