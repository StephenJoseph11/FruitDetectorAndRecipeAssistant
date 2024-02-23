
def get_fruit_counts(result, class_dict):
    print(len(result.boxes))
    print(result.boxes[0])
    for box in result.boxes:
        print(box.data[0])
        print(box.xyxy[0].tolist())

    fruit_counts = {}


    for box in result.boxes:
        class_id = round(box.cls[0].item())  # Round the class ID to the nearest integer
        if class_id in class_dict:
            fruit_name = class_dict[class_id]
            if fruit_name in fruit_counts:
                fruit_counts[fruit_name] += 1
            else:
                fruit_counts[fruit_name] = 1
    print(fruit_counts)
    # Print the fruit counts
    #for fruit_name, count in fruit_counts.items():
    #    print(f"Detected {count} {fruit_name}(s)")
    print(box.xyxy[0].tolist())
    return fruit_counts
