/** @type {import('next').NextConfig} */
const nextConfig = {
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: `${process.env.BACKEND_URL}/api/:path*`
      },
      { 
        source: '/health', 
        destination: `${process.env.BACKEND_URL}/health` 
      }
    ]
  },
  images: { 
    remotePatterns: [] 
  }
}

module.exports = nextConfig
