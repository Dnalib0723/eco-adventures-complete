// API 配置
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';
const API_VERSION = '/api/v1';

export const API_ENDPOINTS = {
  // 課程相關
  COURSES: `${API_BASE_URL}${API_VERSION}/courses`,
  COURSES_UPCOMING: `${API_BASE_URL}${API_VERSION}/courses/upcoming`,
  COURSE_DETAIL: (id: number) => `${API_BASE_URL}${API_VERSION}/courses/${id}`,
  
  // 報名相關
  REGISTRATIONS: `${API_BASE_URL}${API_VERSION}/registrations`,
  REGISTRATION_DETAIL: (id: number) => `${API_BASE_URL}${API_VERSION}/registrations/${id}`,
  REGISTRATION_BY_EMAIL: (email: string) => `${API_BASE_URL}${API_VERSION}/registrations/by-email/${email}`,
  REGISTRATION_CANCEL: (id: number) => `${API_BASE_URL}${API_VERSION}/registrations/${id}/cancel`,
  
  // 講師相關
  INSTRUCTORS: `${API_BASE_URL}${API_VERSION}/instructors`,
  INSTRUCTOR_DETAIL: (id: number) => `${API_BASE_URL}${API_VERSION}/instructors/${id}`,
  
  // 活動相關
  ACTIVITIES: `${API_BASE_URL}${API_VERSION}/activities`,
  ACTIVITY_DETAIL: (id: number) => `${API_BASE_URL}${API_VERSION}/activities/${id}`,
  
  // FAQ 相關
  FAQS: `${API_BASE_URL}${API_VERSION}/faqs`,
  FAQ_DETAIL: (id: number) => `${API_BASE_URL}${API_VERSION}/faqs/${id}`,
};

export default API_ENDPOINTS;
