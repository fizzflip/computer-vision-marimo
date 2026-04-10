import marimo

__generated_with = "0.22.0"
app = marimo.App(width="medium", auto_download=["ipynb", "html"])


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import cv2
    import matplotlib.pyplot as plt

    return cv2, plt


@app.cell
def _(cv2):
    query_img = cv2.imread('/home/mrbot/Documents/devenvs/marimo/article-0-1A1318E1000005DC-594_470x572.jpg')
    train_img = cv2.imread('/home/mrbot/Documents/devenvs/marimo/article-0-1A1318ED000005DC-299_470x572.jpg')

    query_img_bw = cv2.cvtColor(query_img, cv2.COLOR_BGR2GRAY)
    train_img_bw = cv2.cvtColor(train_img, cv2.COLOR_BGR2GRAY)
    return query_img, query_img_bw, train_img, train_img_bw


@app.cell
def _(cv2, query_img_bw, train_img_bw):
    orb = cv2.ORB_create()

    queryKeypoints, queryDescriptors = orb.detectAndCompute(query_img_bw, None)
    trainKeypoints, trainDescriptors = orb.detectAndCompute(train_img_bw, None)
    return queryDescriptors, queryKeypoints, trainDescriptors, trainKeypoints


@app.cell
def _(cv2, queryDescriptors, trainDescriptors):
    matcher = cv2.BFMatcher()
    matches = matcher.match(queryDescriptors, trainDescriptors)
    return (matches,)


@app.cell
def _(cv2, matches, plt, queryKeypoints, query_img, trainKeypoints, train_img):
    final_img = cv2.drawMatches(query_img, queryKeypoints, train_img, trainKeypoints, matches[:20], None)
    final_img = cv2.resize(final_img, (1000, 650))

    plt.figure(figsize=(10, 6))
    plt.imshow(cv2.cvtColor(final_img, cv2.COLOR_BGR2RGB)) 
    plt.title("Feature Matches")
    plt.axis('off')  
    plt.show()
    return


if __name__ == "__main__":
    app.run()
