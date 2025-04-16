import pandas as pd
import os

def stitch_csv_files():
    # Define file paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    crashes_file = os.path.join(current_dir, 'Crashes.csv')
    parties_file = os.path.join(current_dir, 'Parties.csv')
    output_file = os.path.join(current_dir, 'Crashes_Parties_Merged.csv')
    
    # Read the CSV files
    try:
        print(f"Reading crashes data from: {crashes_file}")
        crashes_df = pd.read_csv(crashes_file, skipinitialspace=True)
        
        print(f"Reading parties data from: {parties_file}")
        parties_df = pd.read_csv(parties_file, skipinitialspace=True)
        
        # Print info about the data
        print(f"Crashes data shape: {crashes_df.shape}")
        print(f"Parties data shape: {parties_df.shape}")
        
        print(f"Number of unique CASE_IDs in crashes data: {crashes_df['CASE_ID'].nunique()}")
        print(f"Number of unique CASE_IDs in parties data: {parties_df['CASE_ID'].nunique()}")
        print(f"Total number of party records: {len(parties_df)}")
        
        # Analyze the one-to-many relationship
        party_counts = parties_df.groupby('CASE_ID').size()
        print(f"Average parties per crash: {party_counts.mean():.2f}")
        print(f"Maximum parties per crash: {party_counts.max()}")
        
        # Merge the dataframes on CASE_ID
        # This will create one row for each party, with all crash information repeated
        print("Merging the dataframes on CASE_ID...")
        merged_df = pd.merge(crashes_df, parties_df, on='CASE_ID', how='inner')
        
        # Print info about the merged data
        print(f"Merged data shape: {merged_df.shape}")
        print(f"Number of unique CASE_IDs in merged data: {merged_df['CASE_ID'].nunique()}")
        
        # Create a verification column to confirm the merge worked correctly
        merged_df['VERIFICATION'] = merged_df['CASE_ID'].astype(str) + '_' + merged_df['PARTY_NUMBER'].astype(str)
        print(f"Number of unique VERIFICATION keys: {merged_df['VERIFICATION'].nunique()}")
        
        # Save the merged dataframe to a new CSV file
        print(f"Saving merged data to: {output_file}")
        merged_df.to_csv(output_file, index=False)
        
        print("Stitching completed successfully!")
        return merged_df
        
    except Exception as e:
        print(f"Error stitching the CSV files: {str(e)}")
        return None

if __name__ == "__main__":
    merged_data = stitch_csv_files()
    
    # Optional: Display some additional statistics about the merged data
    if merged_data is not None:
        parties_per_crash = merged_data.groupby('CASE_ID').size()
        print("\nAdditional Statistics:")
        print(f"Distribution of parties per crash:")
        print(parties_per_crash.value_counts().sort_index())
