/** @type {import('next').NextConfig} */
const nextConfig = {
  async rewrites() {
    // Default to localhost for development, will be overridden by BACKEND_URL in production
    const backendUrl = process.env.BACKEND_URL || 'http://localhost:8000'
    
    return [
      {
        source: '/api/:path*',
        destination: `${backendUrl}/api/:path*`
      },
      { 
        source: '/health', 
        destination: `${backendUrl}/health` 
      }
    ]
  },
  images: { 
    remotePatterns: [] 
  }
}

module.exports = nextConfig
