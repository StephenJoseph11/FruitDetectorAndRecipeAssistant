import cv2

def create_bounding_box(image_path, annotated_image_path, result, class_dict):
    image = cv2.imread(image_path)

    for box in result.boxes:
        class_id = round(box.cls[0].item())
        confidence = box.conf[0].item()
        label = class_dict[class_id]
        
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        color = (0, 255, 0)  # Green color for the bounding box
        thickness = 1  # Thickness of the bounding box
        
        # Draw bounding box
        cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), color, thickness)
        
        # Draw label
        cv2.putText(image, f"{label} ({confidence:.2f})", (int(x1)+5, int(y1) + 15),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Convert BGR image to RGB (for displaying with matplotlib)

    annotated_image_path = "static/annotated_image.jpg"
    cv2.imwrite(annotated_image_path, image)
