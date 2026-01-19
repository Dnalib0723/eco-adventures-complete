import API_ENDPOINTS from './api-config';

// API 錯誤類別
export class APIError extends Error {
  constructor(public status: number, message: string) {
    super(message);
    this.name = 'APIError';
  }
}

// 通用 fetch 包裝器
async function fetchAPI<T>(url: string, options: RequestInit = {}): Promise<T> {
  try {
    const response = await fetch(url, {
      ...options,
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
    });

    if (!response.ok) {
      const error = await response.json().catch(() => ({ detail: '未知錯誤' }));
      throw new APIError(response.status, error.detail || '請求失敗');
    }

    return await response.json();
  } catch (error) {
    if (error instanceof APIError) {
      throw error;
    }
    throw new Error('網路錯誤，請檢查連線');
  }
}

// ============ 課程 API ============
export const courseAPI = {
  // 取得課程列表
  getAll: (params?: { skip?: number; limit?: number; status?: string; category?: string }) => {
    const searchParams = new URLSearchParams();
    if (params?.skip) searchParams.set('skip', params.skip.toString());
    if (params?.limit) searchParams.set('limit', params.limit.toString());
    if (params?.status) searchParams.set('status', params.status);
    if (params?.category) searchParams.set('category', params.category);
    
    const url = `${API_ENDPOINTS.COURSES}${searchParams.toString() ? '?' + searchParams.toString() : ''}`;
    return fetchAPI<any[]>(url);
  },

  // 取得即將開始的課程
  getUpcoming: (limit = 10) => {
    return fetchAPI<any[]>(`${API_ENDPOINTS.COURSES_UPCOMING}?limit=${limit}`);
  },

  // 取得單一課程
  getById: (id: number) => {
    return fetchAPI<any>(API_ENDPOINTS.COURSE_DETAIL(id));
  },

  // 建立課程（管理員）
  create: (data: any) => {
    return fetchAPI<any>(API_ENDPOINTS.COURSES, {
      method: 'POST',
      body: JSON.stringify(data),
    });
  },

  // 更新課程（管理員）
  update: (id: number, data: any) => {
    return fetchAPI<any>(API_ENDPOINTS.COURSE_DETAIL(id), {
      method: 'PUT',
      body: JSON.stringify(data),
    });
  },

  // 刪除課程（管理員）
  delete: (id: number) => {
    return fetchAPI<any>(API_ENDPOINTS.COURSE_DETAIL(id), {
      method: 'DELETE',
    });
  },
};

// ============ 報名 API ============
export const registrationAPI = {
  // 建立報名
  create: (data: {
    course_id: number;
    name: string;
    email: string;
    phone: string;
    participants: number;
    notes?: string;
  }) => {
    return fetchAPI<any>(API_ENDPOINTS.REGISTRATIONS, {
      method: 'POST',
      body: JSON.stringify(data),
    });
  },

  // 查詢報名記錄（by email）
  getByEmail: (email: string) => {
    return fetchAPI<any[]>(API_ENDPOINTS.REGISTRATION_BY_EMAIL(email));
  },

  // 取得單一報名記錄
  getById: (id: number) => {
    return fetchAPI<any>(API_ENDPOINTS.REGISTRATION_DETAIL(id));
  },

  // 取消報名
  cancel: (id: number) => {
    return fetchAPI<any>(API_ENDPOINTS.REGISTRATION_CANCEL(id), {
      method: 'POST',
    });
  },

  // 取得報名列表（管理員）
  getAll: (params?: { skip?: number; limit?: number; course_id?: number; status?: string }) => {
    const searchParams = new URLSearchParams();
    if (params?.skip) searchParams.set('skip', params.skip.toString());
    if (params?.limit) searchParams.set('limit', params.limit.toString());
    if (params?.course_id) searchParams.set('course_id', params.course_id.toString());
    if (params?.status) searchParams.set('status', params.status);
    
    const url = `${API_ENDPOINTS.REGISTRATIONS}${searchParams.toString() ? '?' + searchParams.toString() : ''}`;
    return fetchAPI<any[]>(url);
  },
};

// ============ 講師 API ============
export const instructorAPI = {
  // 取得講師列表
  getAll: (params?: { skip?: number; limit?: number; is_active?: boolean }) => {
    const searchParams = new URLSearchParams();
    if (params?.skip) searchParams.set('skip', params.skip.toString());
    if (params?.limit) searchParams.set('limit', params.limit.toString());
    if (params?.is_active !== undefined) searchParams.set('is_active', params.is_active.toString());
    
    const url = `${API_ENDPOINTS.INSTRUCTORS}${searchParams.toString() ? '?' + searchParams.toString() : ''}`;
    return fetchAPI<any[]>(url);
  },

  // 取得單一講師
  getById: (id: number) => {
    return fetchAPI<any>(API_ENDPOINTS.INSTRUCTOR_DETAIL(id));
  },
};

// ============ 活動 API ============
export const activityAPI = {
  // 取得活動列表
  getAll: (params?: { skip?: number; limit?: number; category?: string }) => {
    const searchParams = new URLSearchParams();
    if (params?.skip) searchParams.set('skip', params.skip.toString());
    if (params?.limit) searchParams.set('limit', params.limit.toString());
    if (params?.category) searchParams.set('category', params.category);
    
    const url = `${API_ENDPOINTS.ACTIVITIES}${searchParams.toString() ? '?' + searchParams.toString() : ''}`;
    return fetchAPI<any[]>(url);
  },

  // 取得單一活動
  getById: (id: number) => {
    return fetchAPI<any>(API_ENDPOINTS.ACTIVITY_DETAIL(id));
  },
};

// ============ FAQ API ============
export const faqAPI = {
  // 取得 FAQ 列表
  getAll: (params?: { skip?: number; limit?: number; is_active?: boolean; category?: string }) => {
    const searchParams = new URLSearchParams();
    if (params?.skip) searchParams.set('skip', params.skip.toString());
    if (params?.limit) searchParams.set('limit', params.limit.toString());
    if (params?.is_active !== undefined) searchParams.set('is_active', params.is_active.toString());
    if (params?.category) searchParams.set('category', params.category);
    
    const url = `${API_ENDPOINTS.FAQS}${searchParams.toString() ? '?' + searchParams.toString() : ''}`;
    return fetchAPI<any[]>(url);
  },

  // 取得單一 FAQ
  getById: (id: number) => {
    return fetchAPI<any>(API_ENDPOINTS.FAQ_DETAIL(id));
  },
};
