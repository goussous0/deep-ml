import math 

def distance(point, centroid):
    return math.sqrt(
        sum(
            [ (point[i] - centroid[i])** 2  for i in range(len(point))]
        )
    )


def recenter(points):
    return tuple([
        round(sum( item[i] for item in points)/len(points), 4)
        for i in range(len(points[0]))
    ])

    



def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
    # Your code here
    final_centroids = initial_centroids.copy()

    for i in range(max_iterations):
        cp_map = { i:[] for i,_ in enumerate(final_centroids)}
        new_centroids = []
        for point in points:
            tmp = sorted([(point, centroid, distance(point, centroid)) for centroid in final_centroids], key=lambda x:x[2], reverse=False)[0]

            for i, centroid in enumerate(final_centroids):
                if tmp[1] == centroid:
                    cp_map[i].append(tmp[0])

        for centroid in cp_map:
            new_centroids.append(recenter(cp_map[centroid]))
        final_centroids = new_centroids.copy()

    return final_centroids
