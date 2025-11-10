import type { PageServerLoad } from './$types';


const API_URL = process.env.API_URL!;
const API_TOKEN = process.env.API_TOKEN!;


export const load: PageServerLoad = async ({ fetch }) => {
  try {
    const res = await fetch(`${API_URL}/uploaded-files/`, {
      headers: {
        Authorization: `Token ${API_TOKEN}`
      }
    });
    console.log('status', res.status);

    if (!res.ok) {
      console.error('Error fetching files:', await res.text());
      throw new Error(`Error fetching files: ${res.status}`);
    }
    const data = await res.json();

    return {
      files: data.results
    };
  } catch (error) {
    console.error('Fetch error:', error);
    return {
      files: []
    };
  }
};
