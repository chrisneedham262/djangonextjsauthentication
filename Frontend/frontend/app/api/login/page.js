import axios from "axios"
import cookie from "cookie"

const handler = async (req, res) => {
	if (req.method === "POST") {
		const {username, password} = req.body

		try {
			const response = await axios.post(
				`${process.env.API_URL}/api/token/`,
				{
					username,
					password,
				},
				{
					headers: {
						"Content-Type": "application/json",
					},
				}
			)

			if (response.data.access) {
				res.setHeader("Set-Cookie", [
					cookie.serialize("access", response.data.access, {
						httpOnly: true,
						secure: process.env.NODE_ENV !== "development",
						maxAge: 60 * 60 * 24 * 15,
						sameSite: "Lax",
						path: "/",
					}),
				])

				return res.status(200).json({
					success: true,
				})
			} else {
				res.status(response.status).json({
					error: "Authentication failed",
				})
			}
		} catch (error) {
			console.error('Login error:', error);

			const statusCode = error.response?.status || 500;
			const errorMessage = error.response?.data?.error || 'An unexpected error occurred';

			res.status(statusCode).json({
				error: errorMessage,
			});
		}
	}
}

export default handler
