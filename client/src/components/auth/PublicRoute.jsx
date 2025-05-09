import { Navigate, Outlet } from 'react-router-dom'
import { useAuth } from '../../contexts/AuthContext'
import Loader from '../common/Loader'

export default function PublicRoute() {
  const { user, loading } = useAuth()

  if (loading) return <Loader />

  return !user ? <Outlet /> : <Navigate to="/dashboard" replace />
}