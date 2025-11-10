<script lang="ts">
  export let data: {
    files: {
      id: number;
      file: string;
      uploaded_at: string;
      compressed_content: string | null;
    }[];
  };
</script>

<div class="overflow-x-auto">
  <table class="table table-zebra">
    <thead>
      <tr>
        <th>#</th>
        <th>File</th>
        <th>Uploaded At</th>
        <th>Compressed Content</th>
      </tr>
    </thead>
    <tbody>
      {#each data.files as file, i}
        <tr>
          <th>{i + 1}</th>
          <td>
            <a href={file.file} target="_blank" class="link link-primary">
              {file.file.split('/').pop()}
            </a>
          </td>
          <td>{new Date(file.uploaded_at).toLocaleString()}</td>
          <td>{file.compressed_content ? 'Yes' : 'No'}</td>
        </tr>
      {/each}
    </tbody>
  </table>
</div>
