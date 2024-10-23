import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt

# Step 1: Load the 3D image
def load_3d_image(file_path):
    pcd = o3d.io.read_point_cloud(file_path)
    return pcd

# Step 2: Segment the image (simplified example using voxel downsampling)
def segment_3d_image(pcd, voxel_size=0.05):
    downsampled_pcd = pcd.voxel_down_sample(voxel_size)
    return downsampled_pcd

# Step 3: Project the segmented 3D data into a 2D floor plan
def project_to_2d(pcd):
    points = np.asarray(pcd.points)
    floor_plan = points[:, [0, 2]]  # Keep only X and Z coordinates
    return floor_plan

# Step 4: Visualize and save the floor plan
def visualize_floor_plan(floor_plan, output_file):
    plt.figure(figsize=(10, 10))
    plt.scatter(floor_plan[:, 0], floor_plan[:, 1], s=1, c='black')
    plt.title('2D Floor Plan')
    plt.xlabel('X')
    plt.ylabel('Z')
    plt.axis('equal')
    plt.savefig(output_file)
    plt.show()

# Main function
def main(file_path, output_file):
    pcd = load_3d_image(file_path)
    segmented_pcd = segment_3d_image(pcd)
    floor_plan = project_to_2d(segmented_pcd)
    visualize_floor_plan(floor_plan, output_file)

# Example usage
input_file = 'floor_plan.ply'
output_file = 'output.png'
main(input_file, output_file)
