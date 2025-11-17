import type { PageServerLoad } from "./$types";
import { API_URL, API_TOKEN } from "$env/static/private";

export const load: PageServerLoad = async ({ fetch }) => {
  try {
    const res = await fetch(`${API_URL}/uploaded-files/`, {
      headers: {
        Authorization: `Token ${API_TOKEN}`,
      },
    });
    console.log("status", res.status);

    if (!res.ok) {
      throw new Error(`Error fetching files: ${res.status}`);
    }
    const data = await res.json();

    return {
      files: data.results,
    };
  } catch (error) {
    console.error("Fetch error:", error);
    return {
      files: [],
    };
  }
};
