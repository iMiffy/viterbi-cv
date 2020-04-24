import numpy as np
import cv2

def viterbi(img, out_height, out_width):

    in_image = cv2.imread(img)
    height_input, width_input = in_image.shape[:2]
    out_image = np.copy(in_image)
    delta_row, delta_col = abs(int(out_height - height_input)), abs(int(out_width - width_input))
    row_turn = 0

    for each_dimen in ['col', 'row']:
        if each_dimen == 'row':
            out_image = np.rot90(out_image)
            delta = delta_row
            row_turn += 1
        else:
            delta = delta_col

        if delta > 0:
            for each_iter in range(delta):
                b, g, r = cv2.split(out_image)
                b_energy = np.absolute(cv2.Scharr(b, -1, 1, 0)) + np.absolute(cv2.Scharr(b, -1, 0, 1))
                g_energy = np.absolute(cv2.Scharr(g, -1, 1, 0)) + np.absolute(cv2.Scharr(g, -1, 0, 1))
                r_energy = np.absolute(cv2.Scharr(r, -1, 1, 0)) + np.absolute(cv2.Scharr(r, -1, 0, 1))
                energy_map = r_energy + g_energy + b_energy
                height, width = energy_map.shape

                dp = [[(None, 0) for i in range(width)] for j in range(height)]
                dp[0] = [(None, 1) for i in energy_map[0]]

                for h in range(1, height):
                    for w in range(width):
                        if w == 0:
                            dp[h][w] = (
                                    np.argmin([dp[h-1][w][1], dp[h-1][w+1][1]])
                                    + w, energy_map[h][w] + min(dp[h-1][w][1],
                                                   dp[h-1][w+1][1]
                                                   ))
                        elif w == width - 1:
                            dp[h][w] = (
                                    np.argmin([dp[h-1][w-1][1], dp[h-1][w][1]])
                            + w - 1, energy_map[h][w] + min(dp[h-1][w-1][1],
                                               dp[h-1][w][1]
                                               ))
                        else:
                            dp[h][w] = (
                                    np.argmin([dp[h-1][w-1][1], dp[h-1][w][1],
                                               dp[h-1][w+1][1]]) + w - 1, energy_map[h][w] + min(dp[h-1][w-1][1],
                                dp[h-1][w][1], dp[h-1][w+1][1]
                                ))

                backtrace = []
                cur = np.argmin([i[1] for i in dp[-1]])
                backtrace.append(cur)
                row = height - 1
                while cur is not None:
                    cur = dp[row][cur][0]
                    backtrace.append(cur)
                    row -= 1

                min_energy_idx = backtrace[:-1][::-1]
                m, n = out_image.shape[:2]
                output = np.zeros((m, n-1, 3))

                for row in range(m):
                    col = min_energy_idx[row]
                    output[row, :, 0] = np.delete(out_image[row, :, 0], [col])
                    output[row, :, 1] = np.delete(out_image[row, :, 1], [col])
                    output[row, :, 2] = np.delete(out_image[row, :, 2], [col])
                out_image = np.copy(output)

    if row_turn == 1:
        out_image = np.rot90(out_image, 3)

    return out_image

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--input-image", required=True, help="path to input image")
    ap.add_argument("-c", "--out-height", required=True, help="final height")
    ap.add_argument("-c", "--out-width", required=True, help="final width")
    ap.add_argument("-m", "--output-image", required=True, help="path to output image")
    args = vars(ap.parse_args())

    final_image = viterbi(args['input_image'], args['out_height'],
                          args['out_width'])
    cv2.imwrite(args['output_image'], final_image.astype(np.uint8))
