# Verifly Vercel Deployment Guide

## Overview
This guide covers deploying your Verifly application to Vercel. You have two deployment options:

1. **Frontend-Only**: Deploy only the Next.js frontend to Vercel, with backend hosted elsewhere
2. **Full-Stack**: Deploy both frontend and backend (as Vercel Functions) to Vercel

## Prerequisites

- Vercel account
- GitHub repository with your code
- Database service (PostgreSQL recommended: Supabase, PlanetScale, or Neon)
- Redis service (Upstash recommended)

## Option 1: Frontend-Only Deployment

### Build Settings in Vercel Dashboard:

**Framework Preset**: Next.js

**Root Directory**: `frontend`

**Build Command**: 
```bash
npm run build
```

**Output Directory**: 
```
.next
```

**Install Command**: 
```bash
npm install
```

**Development Command**: 
```bash
npm run dev
```

### Environment Variables (Frontend-Only):

Add these in Vercel Dashboard → Settings → Environment Variables:

```
NEXT_PUBLIC_API_URL=https://your-backend-api.com
NEXT_PUBLIC_FRONTEND_URL=https://your-app.vercel.app
```

## Option 2: Full-Stack Deployment

### Build Settings in Vercel Dashboard:

**Framework Preset**: Next.js

**Root Directory**: Leave empty (project root)

**Build Command**: 
```bash
cd frontend && npm run build
```

**Output Directory**: 
```
frontend/.next
```

**Install Command**: 
```bash
cd frontend && npm install
```

**Development Command**: 
```bash
cd frontend && npm run dev
```

### Environment Variables (Full-Stack):

Add these in Vercel Dashboard → Settings → Environment Variables:

```
# Frontend Variables
NEXT_PUBLIC_API_URL=https://your-app.vercel.app
NEXT_PUBLIC_FRONTEND_URL=https://your-app.vercel.app

# Backend Variables
DATABASE_URL=postgresql://username:password@host:port/database
REDIS_URL=redis://username:password@host:port/database
SECRET_KEY=your-super-secret-key-at-least-32-characters-long
ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_DAYS=7
ENVIRONMENT=production
BACKEND_CORS_ORIGINS=https://your-app.vercel.app

# Python Path
PYTHONPATH=backend
```

## Database Setup

### Recommended Services:

1. **Supabase** (PostgreSQL + Auth):
   ```
   DATABASE_URL=postgresql://postgres:password@db.supabase.co:5432/postgres
   ```

2. **PlanetScale** (MySQL):
   ```
   DATABASE_URL=mysql://username:password@host:port/database
   ```

3. **Neon** (PostgreSQL):
   ```
   DATABASE_URL=postgresql://username:password@host:port/database
   ```

### Database Migration:

For production, you'll need to run migrations. Add this to your deployment:

```bash
# In your backend directory
alembic upgrade head
```

## Redis Setup

### Upstash (Recommended):

1. Create account at [Upstash](https://upstash.com)
2. Create Redis database
3. Copy connection URL:
   ```
   REDIS_URL=rediss://default:password@host:port
   ```

## Deployment Steps

### Step 1: Prepare Your Repository

1. Ensure all configuration files are in place:
   - `vercel.json` (root)
   - `frontend/next.config.js` (updated)
   - `requirements.txt` (root)
   - `api/index.py` (for full-stack)

### Step 2: Deploy to Vercel

#### Option A: Vercel CLI
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel --prod
```

#### Option B: GitHub Integration
1. Connect your GitHub repository to Vercel
2. Configure build settings (as shown above)
3. Set environment variables
4. Deploy automatically on push

### Step 3: Configure Environment Variables

In Vercel Dashboard → Your Project → Settings → Environment Variables:

**For Frontend-Only:**
- `NEXT_PUBLIC_API_URL`
- `NEXT_PUBLIC_FRONTEND_URL`

**For Full-Stack:**
- All frontend variables above
- `DATABASE_URL`
- `REDIS_URL`
- `SECRET_KEY`
- `ACCESS_TOKEN_EXPIRE_MINUTES`
- `REFRESH_TOKEN_EXPIRE_DAYS`
- `ENVIRONMENT`
- `BACKEND_CORS_ORIGINS`
- `PYTHONPATH`

### Step 4: Test Deployment

1. Visit your deployed URL
2. Test registration/login functionality
3. Check browser console for errors
4. Verify API endpoints are working

## Troubleshooting

### Common Issues:

1. **API Routes Not Found (404)**
   - Check `vercel.json` routing configuration
   - Ensure `api/index.py` exists for full-stack deployment

2. **CORS Errors**
   - Update `BACKEND_CORS_ORIGINS` environment variable
   - Check `next.config.js` CORS headers

3. **Database Connection Errors**
   - Verify `DATABASE_URL` format
   - Check database service is accessible
   - Run migrations: `alembic upgrade head`

4. **Build Failures**
   - Check build logs in Vercel dashboard
   - Verify all dependencies are in `requirements.txt`
   - Ensure Python version compatibility

### Debug Commands:

```bash
# Check build logs
vercel logs

# Test locally with production environment
vercel dev

# Check function logs
vercel logs --follow
```

## Performance Optimization

### Frontend:
- Enable Next.js Image Optimization
- Use static generation where possible
- Optimize bundle size

### Backend:
- Use connection pooling for database
- Implement caching with Redis
- Optimize query performance

## Security Checklist

- [ ] Use strong `SECRET_KEY` (32+ characters)
- [ ] Configure CORS origins properly
- [ ] Use HTTPS in production
- [ ] Enable secure cookie settings
- [ ] Set up proper database permissions
- [ ] Use environment variables for secrets

## Monitoring

### Recommended Tools:
- Vercel Analytics (built-in)
- Sentry for error tracking
- LogRocket for user sessions
- Database monitoring from your provider

## Scaling Considerations

### Vercel Limits:
- Function timeout: 30 seconds (can be extended)
- Function size: 50MB
- Bandwidth: Based on plan
- Database connections: Limited by serverless nature

### Alternatives for Heavy Backend:
- Railway
- Render
- Digital Ocean App Platform
- AWS Lambda with API Gateway
