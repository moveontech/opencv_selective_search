import cv2

if __name__ == '__main__':

    cv2.setUseOptimized(True)
    cv2.setNumThreads(4)

    im = cv2.imread("img.jpg")
    # resize image
    newHeight = 200
    newWidth = int(im.shape[1] * 200 / im.shape[0])
    im = cv2.resize(im, (newWidth, newHeight))

    ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()

    ss.setBaseImage(im)

    ss.switchToSelectiveSearchFast()
    # ss.switchToSelectiveSearchQuality()

    rects = ss.process()
    print('Total Number of Region Proposals: {}'.format(len(rects)))

    numShowRects = 100
    increment = 50

    while True:
        imOut = im.copy()

        for i, rect in enumerate(rects):

            if i < numShowRects:
                x, y, w, h = rect
                cv2.rectangle(imOut, (x, y), (x + w, y + h), (0, 255, 0), 1, cv2.LINE_AA)
            else:
                break

        cv2.imshow("Output", imOut)
        cv2.imwrite("output.png", imOut)

        k = cv2.waitKey(0) & 0xFF

        if k == 109:
            # increase total number of rectangles to show by increment
            numShowRects += increment
        # l is pressed
        elif k == 108 and numShowRects > increment:
            # decrease total number of rectangles to show by increment
            numShowRects -= increment
        # q is pressed
        elif k == 113:
            break
    cv2.destroyAllWindows()
