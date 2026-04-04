import cv2
import matplotlib.pyplot as plt


def main():
    # Load image in grayscale mode
    image = cv2.imread("images/sample.png", cv2.IMREAD_GRAYSCALE)

    # Check if image was loaded correctly
    if image is None:
        print("Error: Could not load image. Check the file path.")
        return

    # Create negative image
    negative_image = 255 - image

    # Show original and negative images
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap="gray")
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(negative_image, cmap="gray")
    plt.title("Negative Image")
    plt.axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()